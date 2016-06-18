import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Users(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.User.get_users()
        self.render(res)

class UsersCSV(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self):
        self.render()

class UserSignIn(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self):
        args = ['account', 'password']
        data = self.get_args(args)
        err, res = yield from Service.User.SignIn(data)
        if err: 
            self.render(err)
        else:
            self.render(res)

