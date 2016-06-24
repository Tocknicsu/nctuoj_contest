from req import Service
from service.base import BaseService
from datetime import datetime


class Contest(BaseService):
    def get_contest(self):
        res = (yield self.db.execute("SELECT * FROM contest")).fetchone()
        return (None, res)

    def put_contest(self, data={}):
        required_args = [{
            'name': '+title',
            'type': str,
        }, {
            'name': '+description',
            'type': str,
        }, {
            'name': '+start',
            'type': datetime,
        }, {
            'name': '+end',
            'type': datetime,
        }, {
            'name': '+freeze',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        data['start'] = str(data['start'])
        data['end'] = str(data['end'])
        sql, param = self.gen_update_sql("contest", data)
        res = yield self.db.execute(sql, param)
        return (None, None)



