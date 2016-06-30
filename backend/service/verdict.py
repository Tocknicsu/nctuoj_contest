from req import Service
from service.base import BaseService
from datetime import datetime


class Verdict(BaseService):
    def get_verdict_list(self):
        res = (yield self.db.execute("SELECT * FROM map_verdict_string")).fetchall()
        return (None, res)

