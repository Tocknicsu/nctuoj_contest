from req import Service
import config
import hashlib
from service.base import BaseService

def HashPassword(x):
    hpwd = hashlib.sha512(str(x).encode()).hexdigest() + config.TORNADO_SETTING['password_salt']
    hpwd = hashlib.md5(str(x).encode()).hexdigest()
    return hpwd


class User(BaseService):
    def SignIn(self, data={}):
        required_args = [{
            'name': '+account',
            'type': str,
        }, {
            'name': '+password',
            'type': str,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM users WHERE account=%s", (data['account'],))
        if res.rowcount == 0:
            return ((404, "User Not Exist"), None)
        res = res.fetchone()
        self.log(HashPassword(data['password']))
        if res['password'] != HashPassword(data['password']):
            return ((403, "Wrong Password"), None)
        return (None, res['token'])

    def get_info_by_token(self, data={}):
        required_args = [{
            'name': '+token',
            'type': str,
        },]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM users WHERE token=%s", (data['token'],))
        res = res.fetchone()
        res.pop('password')
        return (None, res)
