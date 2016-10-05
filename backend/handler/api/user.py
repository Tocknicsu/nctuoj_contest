import tornado
import tornado.gen
import os
import config

from req import Service
from req import ApiRequestHandler
from req import StaticFileHandler

class Users(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        data = {
            'type': self.account['type']
        }
        err, res = yield from Service.User.get_user_list(data)
        self.render(res)

    @tornado.gen.coroutine
    def post(self):
        args = ['account', 'name', 'password', 'type']
        data = self.get_args(args)
        err, res = yield from Service.User.post_user(data)
        if err:
            self.render(err)
        else:
            res['account'] = self.account
            err, res = yield from Service.User.get_user(res)
            self.render(res)

class User(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        data = {}
        data['id'] = id
        data['account'] = self.account
        err, res = yield from Service.User.get_user(data)
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def put(self, id):
        args = ['account', 'name', 'password', 'type']
        data = self.get_args(args)
        data['id'] = id
        err, res = yield from Service.User.put_user(data)
        if err:
            self.render(err)
        else:
            data = {}
            data['id'] = id
            data['account'] = self.account
            err, res = yield from Service.User.get_user(data)
            self.render(res)

    @tornado.gen.coroutine
    def delete(self, id):
        data = {}
        data['id'] = id
        err, res = yield from Service.User.delete_user(data)
        if err:
            self.render(err)
        else:
            self.render(res)

class UsersMe(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.render(self.account)

class UsersCode(StaticFileHandler):
    @tornado.gen.coroutine
    def get(self, include_body=True):
        data = {}
        data['user_id'] = self.account['id']
        err, res = yield from Service.Submission.get_submission_zip(data)
        super().get(res, include_body)
        os.remove(os.path.join(config.DATA_ROOT, 'data/tmp', res))


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

class UserUpload(ApiRequestHandler):
    @tornado.gen.coroutine
    def put(self):
        args = ['file[file]', 'new_team', 'follow_rule', 'team']
        data = self.get_args(args)
        data['id'] = self.account['id']
        err, res = yield from Service.User.UploadFile(data)
        if err:
            self.render(err)
        else:
            self.render(res)
