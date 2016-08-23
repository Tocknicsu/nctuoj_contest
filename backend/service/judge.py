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
            'xss': False,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        sql, param = self.gen_insert_sql('map_submission_testdata', data)
        yield self.db.execute(sql, param)
        return (None, None)

    def post_submission(self, data):
        required_args = [{
            'name': '+submission_id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        err, submission = yield from Service.Submission.get_submission({'id': data['submission_id']})
        err, problem = yield from Service.Problem.get_problem({'id': submission['problem_id']})
        submission_testdata = (yield self.db.execute("SELECT * FROM map_submission_testdata WHERE submission_id=%s", (data['submission_id'],))).fetchall()
        data = {}
        data['time_usage'] = max((x['time_usage'] for x in submission_testdata if x['time_usage'] is not None), default=0)
        data['memory_usage'] = max((x['memory_usage'] for x in submission_testdata if x['memory_usage'] is not None), default=0)
        data['verdict_id'] = min((x['verdict_id'] for x in submission_testdata), default=10)
        if problem['score_type'] == 0: #sum
            data['score'] = sum(x['score'] for x in submission_testdata)
        elif problem['score_type'] == 1: #min
            data['score'] = min(x['score'] for x in submission_testdata)
        else:
            data['score'] = 0
        self.log(data)
        sql, param = self.gen_update_sql('submissions', data)
        yield self.db.execute(sql + ' WHERE id = %s;', param + (submission['id'],))
        return (None, None)

        

