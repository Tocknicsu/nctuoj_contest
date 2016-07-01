from req import Service
from service.base import BaseService
import config
import os
import shutil


class Problem(BaseService):
    def get_problem_list(self):
        res = yield self.db.execute("SELECT * FROM problems ORDER BY id ASC")
        res = res.fetchall()
        return (None, res)

    def get_problem(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM problems WHERE id=%s", (data['id'],))
        res = res.fetchone()
        return (None, res)

    def get_problem_detail(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM problems WHERE id=%s", (data['id'],))
        res = res.fetchone()
        err, res['executes'] = yield from self.get_problem_execute(data)
        err, res['testdata'] = yield from Service.Testdata.get_testdata_list(data)
        err, res['verdict'] = yield from self.get_problem_verdict(data)
        return (None, res)

    def post_problem(self, data={}):
        required_args = [{
            'name': '+title',
            'type': str,
        }, {
            'name': '+score_type',
            'type': int
        }, {
            'name': '+pdf',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        pdf = data.pop('pdf')
        sql, param = self.gen_insert_sql('problems', data)
        res = yield self.db.execute(sql, param)
        res = res.fetchone()
        ### Save File
        folder = '%s/data/problems/%s'%(config.DATA_ROOT, str(res['id']))
        file_path = '%s/pdf.pdf'%(folder)
        try: os.makedirs(folder)
        except: pass
        with open(file_path, 'wb+') as f:
            f.write(pdf['body'])
        ### Add default verdict
        yield self.db.execute("INSERT INTO verdicts (id, file_name, execute_type_id) VALUES (%s, %s, %s)", (res['id'], "main.cpp", 2,))
        ### copy default verdict file
        folder = '%s/data/verdicts/%s/'%(config.DATA_ROOT, str(res['id']))
        file_path = '%s/%s'%(folder, "main.cpp")
        try: os.makedirs(folder)
        except: pass
        shutil.copyfile("./default/verdict/main.cpp", file_path)
        return (None, res)

    def put_problem(self, data):
        required_args = [{
            'name': '+id',
            'type': int
        }, {
            'name': '+title',
            'type': str,
        }, {
            'name': '+score_type',
            'type': int
        }, {
            'name': 'pdf',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        if 'pdf' in data:
            pdf = data.pop('pdf')
        else:
            pdf = None
        id = data.pop('id')
        sql, param = self.gen_update_sql('problems', data)
        res = yield self.db.execute(sql + ' WHERE id = %s', param + (id,))
        if pdf:
            folder = '%s/data/problems/%s'%(config.DATA_ROOT, str(id))
            file_path = '%s/pdf.pdf'%(folder)
            try: os.makedirs(folder)
            except: pass
            with open(file_path, 'wb+') as f:
                f.write(pdf['body'])
        return (None, None)

    def get_problem_execute(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT e.id, e.description FROM map_problem_execute as me, execute_types as e WHERE e.id=me.execute_type_id and me.problem_id=%s", (data['id'],))
        res = res.fetchall()
        return (None, res)

    def put_problem_execute(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int
        }, {
            'name': '+executes',
            'type': list
        }]
        self.log(data)
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        yield self.db.execute("DELETE FROM map_problem_execute WHERE problem_id=%s", (data['id'],))
        for x in data['executes']:
            try:
                yield self.db.execute("INSERT INTO map_problem_execute (problem_id, execute_type_id) VALUES (%s, %s)", (data['id'], x,))
            except:
                pass
        return (None, None)

    def get_problem_verdict(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM verdicts WHERE id=%s", (data['id'],))
        res = res.fetchone()
        return (None, res)

    def put_problem_verdict(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }, {
            'name': '+execute_type_id',
            'type': int,
        }, {
            'name': 'file',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        yield self.db.execute("UPDATE verdicts SET execute_type_id=%s WHERE id=%s",(data['execute_type_id'], data['id']))
        if data['file'] is not None:
            code_file = data.pop('file')
            data['file_name'] = code_file['filename']
            yield self.db.execute("UPDATE verdicts SET file_name=%s WHERE id=%s",(data['file_name'], data['id'],))
            folder = '%s/data/verdicts/%s/'%(config.DATA_ROOT, id)
            file_path = '%s/%s'%(folder, data['file_name'])
            try: shutil.rmtree(folder)
            except: pass
            try: os.makedirs(folder)
            except: pass
            with open(file_path, 'wb+') as f:
                f.write(code_file['body'])
        return (None, None)
