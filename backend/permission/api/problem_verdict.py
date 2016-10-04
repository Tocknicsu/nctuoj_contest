from req import Service
from permission.base import BasePermission

class ProblemVerdict(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Problem.get_problem(data)
        if res is None:
            return (404, "Not Found")

    def get(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
        err = yield from self.exist({'id': id})
        if err:
            return err

    def put(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
        err = yield from self.exist({'id': id})
        if err:
            return err

class ProblemVerdictFile(BasePermission):
    def get(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
