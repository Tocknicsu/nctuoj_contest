from req import Service
from permission.base import BasePermission

class Submissions(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Problem.get_problem_execute(data)
        if res is None:
            return (404, "Not Found")

    def get(self, req):
        pass

    def post(self, req):
        if not req.account['isLOGIN']:
            return (403, "Permission Denied")
        err = yield from self.exist(data)
        if err:
            return err



class Submission(BasePermission):
    def exist(self, data={}):
        pass

    def get(self, req, id):
        pass
