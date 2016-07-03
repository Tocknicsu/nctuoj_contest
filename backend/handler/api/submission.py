import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler
from req import StaticFileHandler

class Submissions(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        if self.account['isADMIN']:
            args = ['problem_id', 'user', 'verdict_id', 'count', 'page']
            data = self.get_args(args)
            err, res = yield from Service.Submission.get_submission_list_admin(data)
        else:
            args = ['count', 'page']
            data = self.get_args(args)
            data['user_id'] = self.account['id']
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
        if data['file'] == None:
            data.pop('file')
            err, res = yield from Service.Submission.post_submission_code(data)
        else:
            data.pop('code')
            data.pop('file_name')
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

class SubmissionFile(StaticFileHandler):
    @tornado.gen.coroutine
    def get(self, id, include_body=True):
        path = ''
        err, res = yield from Service.Problem.get_problem_verdict({'id': id})
        err, res = yield from Service.Submission.get_submission({'id': id})
        path = '%s/%s' % (id, res['file_name'])
        yield super().get(path, include_body)
