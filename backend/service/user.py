from req import Service
import config
import hashlib
import csv
import io
import time
from service.base import BaseService

def HashPassword(x):
    hpwd = hashlib.sha512(str(x).encode()).hexdigest() + config.TORNADO_SETTING['password_salt']
    hpwd = hashlib.md5(str(hpwd).encode()).hexdigest()
    return str(hpwd)

def GenToken(account):
    token = []
    token.append('CONTEST')
    token.append(hashlib.md5(account['account'].encode()).hexdigest()[:10])
    token.append(hashlib.md5((account['password'] + str(time.time())).encode()).hexdigest()[:40])
    return '@'.join(token)


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

    def get_user_by_token(self, data={}):
        required_args = [{
            'name': '+token',
            'type': str,
        },]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM users WHERE token=%s", (data['token'],))
        if res.rowcount == 0:
            return ((403, 'no such user'), None)
        res = res.fetchone()
        res.pop('password')
        return (None, res)

    def get_user(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        },]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT * FROM users WHERE id=%s", (data['id'],))
        if res.rowcount == 0:
            return ((403, 'no such user'), None)
        res = res.fetchone()
        res.pop('password')
        return (None, res)
    
    def get_users(self, data={}):
        required_args = [{
            'name': '+account',
            'type': dict,
        },]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute('SELECT * FROM users WHERE "type" >= %s;', (data['account']['type'],))
        res = res.fetchall()
        return (None, res)

    def post_user(self, data={}):
        required_args = [{
            'name': '+account',
            'type': str,
        }, {
            'name': '+name',
            'type': str,
        }, {
            'name': '+password',
            'type': str,
        }, {
            'name': '+repassword',
            'type': str,
        }, {
            'name': 'type',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute('SELECT 1 FROM users WHERE account = %s OR name = %s;', (data['account'], data['name'],))
        if res.rowcount != 0:
            return ((400, 'account or name exists'), None)
        if data['password'] != data['repassword']:
            return ((400, 'confirm your password'), None)
        data.pop('repassword')
        data['password'] = HashPassword(data['password'])
        data['token'] = GenToken(data)
        sql, param = self.gen_insert_sql('users', data)
        res = yield self.db.execute(sql, param)
        return (None, res.fetchone()['id'])


    def gen_users_by_csv(self, data={}):
        '''
        account,name,password,type
        '''
        required_args = [{
            'name': 'users_file',    
        },]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        users = list(csv.DictReader(io.StringIO(data['users_file']['body'].decode()), ['account', 'name', 'password', 'type']))
        res = {}
        res['error'] = []
        res['success'] = []
        for user in users:
            user['repassword'] = user['password']
            err, id = yield from self.post_user(user)
            if err:
                user['err_msg'] = err[1]
                res['error'].append(user)
            else:
                user['id'] = id
                res['success'].append(user)

        return (None, res)
