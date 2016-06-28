import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Clarifications(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Clarification.get_clarification_list()
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def post(self):
        args = ['problem_id', 'question']
        data = self.get_args(args)
        data['user_id'] = self.account['id']
        err, res = yield from Service.Clarification.post_clarification(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Clarification.get_clarification(res)
            self.render(res)

class Clarification(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        err, res = yield from Service.Clarification.get_clarification({'id': id})
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, id):
        args = ['reply_type', 'reply']
        data = self.get_args(args)
        data['id'] = id
        err, res = yield from Service.Clarification.put_clarification(data)
        if err:
            self.render(err)
        else:
            err, res = yield from Service.Clarification.get_clarification({'id': id})
            self.render(res)
        
