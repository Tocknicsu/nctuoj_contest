from req import Service
from service.base import BaseService
import config
import os
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
            'name': 'user',
            'type': str,
        }, {
            'name': 'problem_id',
            'type': int,
        }, {
            'name': 'verdict_id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        where = {}
        if data['user'] is not None:
            pass
        if data['problem_id'] is not None:
            pass
        if data['verdict_id'] is not None:
            pass

        self.log(data)
        limit, offset = self.calc_limit_offset(data['page'], data['count'])
        res = {}
        res['data'] = (yield self.db.execute("SELECT * FROM submissions ORDER BY id DESC LIMIT %s OFFSET %s", (limit, offset,))).fetchall()
        res['count'] = (yield self.db.execute("SELECT COUNT(*) as count FROM submissions")).fetchone()['count']
        return (None, res)

    def get_submission_list(self, data={}):
        required_args = [{
            'name': '+count',
            'type': int,
        }, {
            'name': '+page',
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
        folder = '%s/data/submissions/%s/'%(config.DATA_ROOT, res['id'])
        file_path = '%s/%s'%(folder, data['file_name'])
        try: os.makedirs(folder)
        except: pass
        with open(file_path, 'w+') as f:
            f.write(code)
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
        folder = '%s/data/submissions/%s/'%(config.DATA_ROOT, res['id'])
        file_path = '%s/%s'%(folder, data['file_name'])
        try: os.makedirs(folder)
        except: pass
        with open(file_path, 'wb+') as f:
            f.write(code_file['body'])
        return (None, res)

