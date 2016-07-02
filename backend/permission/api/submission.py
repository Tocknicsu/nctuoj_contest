from req import Service
from permission.base import BasePermission

class Submissions(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Problem.get_problem_execute(data)
        if err: 
            return err
        if res is None:
            return (404, "Not Found")

    def get(self, req):
        pass

    def post(self, req):
        if not req.account['isLOGIN']:
            return (403, "Permission Denied")
        args = ['problem_id', 'execute_type_id']
        data = req.get_args(args)
        self.log(data)
        err = yield from self.exist(data)
        if err:
            return err
        if req.account['isADMIN']:
            return None
        err, res = yield from Service.Util.contest_status()
        ### 0 is in contest time
        if res != 0: 
            return (403, "Permission Denied")





class Submission(BasePermission):
    def exist(self, data={}):
        err, res = yield from Service.Submission.get_submission({'id': data['id']})
        if err:
            return err
        if res is None:
            return (404, "Not Found")
        pass

    def get(self, req, id):
        if not req.account['isLOGIN']:
            return (403, "Permission Denied")
        err = yield from self.exist({'id': id})
        if err:
            return err
        if req.account['isADMIN']:
            return 
        if int(req.account['id']) != int(res['user_id']):
            return (403, "Permission Denied")

