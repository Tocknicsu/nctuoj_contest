from req import Service
from service.base import BaseService

import os
import config


class Testdata(BaseService):
    def get_testdata_list(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM testdata WHERE problem_id=%s ORDER BY id ASC", (data['id'],))
        res = res.fetchall()
        return (None, res)

    def get_testdata(self, data={}):
        self.log(data)
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM testdata WHERE id=%s ORDER BY id ASC", (data['id'],))
        res = res.fetchone()
        return (None, res)
        

    def post_testdata(self, data={}):
        required_args = [{
            'name': '+problem_id',
            'type': int,
        }, {
            'name': '+score',
            'type': int,
        }, {
            'name': '+time_limit',
            'type': int,
        }, {
            'name': '+memory_limit',
            'type': int,
        }, {
            'name': '+output_limit',
            'type': int,
        }, {
            'name': 'input'
        }, {
            'name': 'output'
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        files = {}
        files['input'] = data.pop('input')
        files['output'] = data.pop('output')
        sql, param = self.gen_insert_sql('testdata', data)
        res = yield self.db.execute(sql, param)
        res = res.fetchone()
        folder = '%s/data/testdata/%s'%(config.DATA_ROOT, res['id'])
        try: os.makedirs(folder)
        except: pass
        for x in files:
            file_path = '%s/%s'%(folder, x)
            with open(file_path, 'wb+') as f:
                if files[x] == None:
                    f.write(''.encode())
                else:
                    f.write(data[x]['body'])
        return (None, res)

    def put_testdata(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }, {
            'name': '+score',
            'type': int,
        }, {
            'name': '+time_limit',
            'type': int,
        }, {
            'name': '+memory_limit',
            'type': int,
        }, {
            'name': '+output_limit',
            'type': int,
        }, {
            'name': 'input'
        }, {
            'name': 'output'
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        files = {}
        files['input'] = data.pop('input')
        files['output'] = data.pop('output')
        id = data.pop('id')
        sql, param = self.gen_update_sql('testdata', data)
        res = yield self.db.execute(sql + ' WHERE id = %s', param + (id,))
        folder = '%s/data/testdata/%s'%(config.DATA_ROOT, data['id'])
        try: os.makedirs(folder)
        except: pass
        for x in files:
            file_path = '%s/%s'%(folder, x)
            with open(file_path, 'wb+') as f:
                if files[x] == None:
                    pass
                else:
                    f.write(data[x]['body'])
        return (None, None)

    def delete_testdata(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        yield self.db.execute("DELETE FROM testdata WHERE id=%s", (data['id'],))
        return (None, res)
