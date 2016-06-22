from req import Service
from service.base import BaseService


class Contest(BaseService):
    def get_contest(self):
        res = (yield self.db.execute("SELECT * FROM contest")).fetchone()
        return (None, res)

