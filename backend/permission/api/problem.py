from req import Service
from permission.base import BasePermission

class Problems(BasePermission):
    def get(self, req):
        pass

    def post(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")


class Problem(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Problem.get_problem(data)
        if res is None:
            return (404, "Not Found")
    
    def get(self, req, id):
        err = yield from self.exist({'id': id})
        if err:
            return err

    def put(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
        err = yield from self.exist({'id': id})
        if err:
            return err

class ProblemsMeta(BasePermission):
    def post(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

class ProblemMeta(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Problem.get_problem(data)
        if res is None:
            return (404, "Not Found")

    def put(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
