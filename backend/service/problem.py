from req import Service
from service.base import BaseService


class Problem(BaseService):
    def get_problem_list(self):
        res = yield self.db.execute("SELECT * FROM problems ORDER BY id ASC")
        res = res.fetchall()
        return (None, res)

