import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Submissions(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        args = ['problem_id', 'user', 'verdict']
        data = self.get_args(args)
        err, res = yield from Service.Submission.get_submission_list(data)
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def post(self):
        args = ['problem_id', 'execute_type_id', 'file_name', 'code', 'file[file]']
        data = self.get_args(args)
        data['user_id'] = self.account['id']
        data['ip'] = self.remote_ip
        self.log(data)
        if data['file'] == None:
            err, res = yield from Service.Submission.post_submission_code(data)
        else:
            err, res = yield from Service.Submission.post_submission_file(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Submission.get_submission(res)
            self.render(res)

class Submission(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        err, res = yield from Service.Submission.get_submission({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)

