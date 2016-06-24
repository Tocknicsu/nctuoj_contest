from req import Service
from service.base import BaseService
import config
import os


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
        self.log(res)
        folder = '%s/data/problems/%s'%(config.DATA_ROOT, str(res['id']))
        file_path = '%s/pdf.pdf'%(folder)
        try: os.makedirs(folder)
        except: pass
        with open(file_path, 'wb+') as f:
            f.write(pdf['body'])
        return (None, res)

    def put_problem(self):
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
            'name': '+pdf',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        pdf = data.pop('pdf')
        sql, param = self.gen_update_sql('problems', data)
        res = yield self.db.execute(sql, param)
        folder = '%s/data/problems/%s'%(config.DATA_ROOT, str(res['id']))
        file_path = '%s/pdf.pdf'%(folder)
        try: os.makedirs(folder)
        except: pass
        with open(file_path, 'wb+') as f:
            f.write(pdf['body'])
        return (None, None)
