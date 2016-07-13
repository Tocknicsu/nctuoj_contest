from req import Service
from permission.base import BasePermission

class Clarifications(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Problem.get_problem(data)
        if err:
            return err
        if int(data['id']) == 0:
            return 
        if res is None:
            return (404, "Not Found")

    def post(self, req):
        if not req.account['isLOGIN']:
            return (403, "Permission Denied")
        args = ['problem_id']
        data = req.get_args(args)
        data = {
            'id': data['problem_id']
        }
        err = yield from self.exist(data)
        if err:
            return err
        return None


class Clarification(BasePermission):
    def put(self, req, id):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
        err, res = yield from Service.Clarification.get_clarification({"id": id})
        if res is None:
            return (404, "Not Found")
        if len(res['reply']):
            return (403, "Permission Denied")
        return None
