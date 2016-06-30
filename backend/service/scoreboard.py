from req import Service
from service.base import BaseService
from datetime import datetime


class Scoreboard(BaseService):
    def get_scoreboard(self, data={}):
        required_args = [{
            'name': '+type',
            'type': str,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = (yield self.db.execute("SELECT * FROM scoreboard WHERE id=%s", (data['type'],))).fetchone()
        return (None, res)

    def put_scoreboard(self, data={}):
        return (None, None)
