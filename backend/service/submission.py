from req import Service
from service.base import BaseService
import config
import os


class Submission(BaseService):
    def get_submission_list(self, data={}):
        pass

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

