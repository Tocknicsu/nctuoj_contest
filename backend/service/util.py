from req import Service
from service.base import BaseService
import datetime


class Util(BaseService):
    ### -1 => before contest
    ### 0  => in contest
    ### 1  => after contest
    def contest_status(self):
        res = (yield self.db.execute("SELECT * FROM contest")).fetchone()
        now = datetime.datetime.now()
        if now < res['start']:
            status = -1
        elif now < res['end']:
            status = 0
        else:
            status = 1
        return (None, status)
