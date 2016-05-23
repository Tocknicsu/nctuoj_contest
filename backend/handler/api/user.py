import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class UserSignIn(ApiRequestHandler):
    @tornado.gen.coroutine
    def post(self):
        args = ['account', 'password']
        data = self.get_args(args)
        self.log(data)
        err, res = yield from Service.User.SignIn(data)
        self.log(str(err)+str( res))
        if err: 
            self.render(err)
        else:
            self.render(res)

