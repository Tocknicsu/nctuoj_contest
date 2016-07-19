from req import Service
from service.base import BaseService

class Rejudge(BaseService):
    def rejudge_submission(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        yield self.db.execute('INSERT INTO wait_submissions (submission_id) VALUES(%s);', (data['id'],))
        yield self.db.execute('UPDATE submissions SET time_usage=%s, memory_usage=%s, score=%s, verdict_id=%s WHERE id=%s;', (None, None, None, 1, data['id']))
        yield self.db.execute('DELETE FROM map_submission_testdata WHERE submission_id=%s;', (data['id'],))
        return (None, None)

    def rejudge_problem(self, data={}):
        required_args = [{
            'name': 'id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute('SELECT s.id FROM submissions as s WHERE s.problem_id=%s ORDER BY s.id ASC;', (data['id'],))
        res = res.fetchall()
        yield self.db.execute('UPDATE submissions SET time_usage=%s, memory_usage=%s, score=%s, verdict_id=%s WHERE id IN %s;', (None, None, None, 1, tuple(x['id'] for x in res)))
        yield self.db.execute('DELETE FROM map_submission_testdata WHERE submission_id IN %s;', (tuple(x['id'] for x in res),))
        yield self.db.execute('INSERT INTO wait_submissions (submission_id) VALUES '+','.join('(%s)'%x['id'] for x in res))
        return (None, None)

