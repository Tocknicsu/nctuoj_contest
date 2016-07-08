from req import Service
from service.base import BaseService
import config
import time
import hashlib
import os
import zipfile
import re


class Submission(BaseService):
    def get_submission_list_admin(self, data={}):
        required_args = [{
            'name': '+count',
            'type': int,
        }, {
            'name': '+page',
            'type': int,
        }, {
            'name': 'user_id',
            'type': str,
        }, {
            'name': 'problem_id',
            'type': int,
        }, {
            'name': 'verdict_id',
            'type': int,
        }]
        self.log(data)
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        where = {}
        cond_sql, param = ' WHERE 1=1 ', ()
        if 'user_id' in data and data['user_id'] is not None:
            cond_sql += ' AND user_id = %s'
            param = param + (data['user_id'],)
        if 'problem_id' in data and data['problem_id'] is not None:
            cond_sql += ' AND problem_id = %s'
            param = param + (data['problem_id'],)
        if 'verdict_id' in data and data['verdict_id'] is not None:
            cond_sql += ' AND verdict_id = %s'
            param = param + (data['verdict_id'],)

        limit, offset = self.calc_limit_offset(data['page'], data['count'])
        res = {}
        res['data'] = (yield self.db.execute("SELECT * FROM submissions " + cond_sql + " ORDER BY id DESC LIMIT %s OFFSET %s", param + (limit, offset,))).fetchall()
        res['count'] = (yield self.db.execute("SELECT COUNT(*) as count FROM submissions " + cond_sql, param)).fetchone()['count']
        return (None, res)

    def get_submission_list(self, data={}):
        required_args = [{
            'name': '+count',
            'type': int,
        }, {
            'name': '+page',
            'type': int,
        }, {
            'name': '+user_id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        limit, offset = self.calc_limit_offset(data['page'], data['count'])
        res = {}
        res['data'] = (yield self.db.execute("SELECT * FROM submissions WHERE user_id=%s ORDER BY id DESC LIMIT %s OFFSET %s", (data['user_id'], limit, offset,))).fetchall()
        res['count'] = (yield self.db.execute("SELECT COUNT(*) as count FROM submissions WHERE user_id=%s", (data['user_id'],))).fetchone()['count']
        return (None, res)

    def get_submission(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM submissions WHERE id=%s", (data['id'],))
        res = res.fetchone()
        res['code'] = open(os.path.join(config.DATA_ROOT, 'data/submissions', str(res['id']), res['file_name'])).read()
        res['testdata'] = (yield self.db.execute('SELECT * FROM map_submission_testdata WHERE submission_id = %s;', (res['id'],))).fetchall()
        return (None, res)

    def fixed_file_name(self, file_name):
        pass

    def post_submission_code(self, data={}):
        required_args = [{
            'name': '+problem_id',
            'type': int,
        }, {
            'name': '+user_id',
            'type': int,
        }, {
            'name': '+execute_type_id',
            'type': int,
        }, {
            'name': '+code',
            'type': str,
        }, {
            'name': '+file_name',
            'type': str,
        }, {
            'name': '+ip',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        if data['file_name'] == '':
            err, res = yield from Service.Execute.get_execute({'id': data['execute_type_id']})
            data['file_name'] = res['file_name']
        code = data.pop('code')
        data['length'] = len(code)
        sql, param = self.gen_insert_sql("submissions", data)
        res = yield self.db.execute(sql, param)
        res = res.fetchone()
        folder = os.path.join(config.DATA_ROOT, 'data/submissions' , str(res['id']))
        file_path = os.path.join(folder, data['file_name'])
        try: os.makedirs(folder)
        except: pass
        with open(file_path, 'w+') as f:
            f.write(code)
        yield self.db.execute("INSERT INTO wait_submissions (submission_id) VALUES (%s)", (res['id'],))
        return (None, res)

    def post_submission_file(self, data={}):
        required_args = [{
            'name': '+problem_id',
            'type': int,
        }, {
            'name': '+user_id',
            'type': int,
        }, {
            'name': '+execute_type_id',
            'type': int,
        }, {
            'name': '+file',
        }, {
            'name': '+ip',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        code_file = data.pop('file')
        data['file_name'] = code_file['filename']
        data['length'] = len(code_file['body'])
        sql, param = self.gen_insert_sql("submissions", data)
        res = yield self.db.execute(sql, param)
        res = res.fetchone()
        folder = os.path.join(config.DATA_ROOT, 'data/submissions', str(res['id']))
        file_path = os.path.join(folder, data['file_name'])
        try: os.makedirs(folder)
        except: pass
        with open(file_path, 'wb+') as f:
            f.write(code_file['body'])
        yield self.db.execute("INSERT INTO wait_submissions (submission_id) VALUES (%s)", (res['id'],))
        return (None, res)

    def get_submission_zip(self, data={}):
        required_args = [{
            'name': '+user_id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err:
            return (err, None)
        res = yield self.db.execute('SELECT id, file_name FROM submissions WHERE user_id = %s;', (data['user_id'],))
        submissions = res.fetchall()
        temp_file_name = '%s.zip' % hashlib.md5(str(time.time()).encode()).hexdigest()
        temp_file_path = os.path.join('/tmp', temp_file_name)
        with zipfile.ZipFile(temp_file_path, 'w', zipfile.ZIP_DEFLATED) as z:
            for submission in submissions:
                file_path = os.path.join(config.DATA_ROOT, 'data/submissions', str(submission['id']), submission['file_name'])
                zip_path = os.path.join(str(submission['id']), submission['file_name'])
                try:
                    z.write(file_path, zip_path)
                except Exception as e:
                    self.log(e)
        return (None, temp_file_name)

