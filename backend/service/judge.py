from req import Service
from service.base import BaseService
import config
import os
import re


class Judge(BaseService):
    def get_submission(self):
        res = yield self.db.execute("DELETE FROM wait_submissions WHERE id IN (SELECT id FROM wait_submissions ORDER BY id LIMIT 1) RETURNING submission_id")
        #res = yield self.db.execute("SELECT submission_id FROM wait_submissions LIMIT 1");
        res = res.fetchone()
        return (None, res)
    def post_submission_testdata(self, data):
        required_args = [{
            'name': '+submission_id',
            'type': int,
        }, {
            'name': '+testdata_id',
            'type': int,
        }, {
            'name': '+verdict_id',
            'type': int,
        }, {
            'name': 'score',
            'type': int,
        }, {
            'name': 'memory_usage',
            'type': int,
        }, {
            'name': 'time_usage',
            'type': int,
        }, {
            'name': 'note',
            'type': str,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        sql, param = self.gen_insert_sql('map_submission_testdata', data)
        yield self.db.execute(sql, param)
        return (None, None)

