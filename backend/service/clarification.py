from req import Service
from service.base import BaseService


class Clarification(BaseService):
    def get_clarification_list(self):
        res = yield self.db.execute("SELECT * FROM clarifications ORDER BY id ASC")
        res = res.fetchall()
        return (None, res)

    def get_clarification(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM clarifications WHERE id=%s", (data['id'],))
        res = res.fetchone()
        return (None, res)

    def post_clarification(self, data={}):
        required_args = [{
            'name': '+user_id',
            'type': int,
        }, {
            'name': '+problem_id',
            'type': int,
        }, {
            'name': '+question',
            'type': str,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        sql, param = self.gen_insert_sql('clarifications', data)
        res = yield self.db.execute(sql, param)
        res = res.fetchone()
        return (None, res)

    def put_clarification(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }, {
            'name': '+reply',
            'type': str,
        }, {
            'name': '+reply_type',
            'type': int,
            'range': (0, 1)
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        id = data.pop('id')
        sql, param = self.gen_update_sql('clarifications', data)
        res = yield self.db.execute(sql + ' WHERE id = %s', param + (id,))
        return (None, None)

