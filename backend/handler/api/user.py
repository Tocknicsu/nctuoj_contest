import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Users(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        data = {}
        data['account'] = self.account
        err, res = yield from Service.User.get_user_list(data)
        self.render(res)

    @tornado.gen.coroutine
    def post(self):
        args = ['account', 'name', 'password', 'repassword', 'type']
        data = self.get_args(args)
        err, res = yield from Service.User.post_user(data)
        if err:
            self.render(err)
        else:
            self.render(res)

class UsersMe(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.render(self.account)

class UsersCSV(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self):
        args = ['users_file[file]']
        data = self.get_args(args)
        err, res = yield from Service.User.gen_users_by_csv(data)
        if err:
            self.render(err)
        else:
            self.render(res)

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

