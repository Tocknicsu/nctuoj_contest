from req import Service
import config
import hashlib
import csv
import io
import time
import os
import shutil
import zipfile
from service.base import BaseService
from map import *

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
        err, res = yield from self.get_user_by_token(res)
        res['isLOGIN'] = True
        return (None, res)

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
        res['isLOGIN'] = True
        for x in map_users_type:
            res['is'+x] = 'type' in res and res['type'] == map_users_type[x]
        return (None, res)

    def get_user(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }, {
            'name': '+account',
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute('SELECT * FROM users WHERE id=%s AND "type" >= %s', (data['id'], data['account']['type']))
        if res.rowcount == 0:
            return ((403, 'no such user'), None)
        res = res.fetchone()
        res.pop('password')
        if data['account']['isADMIN'] or (data['account']['isLOGIN'] and int(data['account']['id']) == int(id)):
            pass
        else:
            res.pop('token')
        res['isLOGIN'] = False
        for x in map_users_type:
            res['is'+x] = 'type' in res and res['type'] == map_users_type[x]
        return (None, res)

    def put_user(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        },{
            'name': '+account',
            'non_empty': True,
            'type': str,
        }, {
            'name': '+name',
            'non_empty': True,
            'type': str,
        }, {
            'name': '+type',
            'type': int,
        }, {
            'name': 'password',
            'type': str,
        }]
        err = self.form_validation(data, required_args)
        if err:
            return (err, None)
        id = data.pop('id')
        if data['password']:
            data['password'] = HashPassword(data['password'])
            data['token'] = GenToken(data)

        sql, param = self.gen_update_sql('users', data)
        yield self.db.execute(sql + ' WHERE id = %s;', param + (id,))
        return (None, None)
    
    def get_user_list(self, data={}):
        required_args = [{
            'name': '+type',
            'type': int,
        },]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute('SELECT id, account, name, "type" FROM users WHERE "type" >= %s;', (data['type'],))
        res = res.fetchall()
        return (None, res)

    def post_user(self, data={}):
        required_args = [{
            'name': '+account',
            'type': str,
            'non_empty': str,
        }, {
            'name': '+name',
            'type': str,
            'non_empty': str,
        }, {
            'name': '+password',
            'type': str,
        }, {
            'name': '+type',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute('SELECT 1 FROM users WHERE account = %s OR name = %s;', (data['account'], data['name'],))
        if res.rowcount != 0:
            return ((400, 'account or name exists'), None)
        data['password'] = HashPassword(data['password'])
        data['token'] = GenToken(data)
        sql, param = self.gen_insert_sql('users', data)
        res = yield self.db.execute(sql, param)
        return (None, {'id': res.fetchone()['id']})

    def delete_user(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err:
            return (err, None)
        yield self.db.execute('DELETE FROM users WHERE id = %s;', (data['id'],))
        return (None, data)

    def gen_users_by_csv(self, data={}):
        '''
        account,name,password,type
        '''
        required_args = [{
            'name': 'users_file',    
        },]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        try:
            users = list(csv.DictReader(io.StringIO(data['users_file']['body'].decode()), ['account', 'name', 'password', 'type']))
        except:
            return ((400, 'csv file broken'), None)
        yield self.db.execute('DELETE FROM users WHERE "type" != 0;')
        res = {}
        res['error'] = []
        res['success'] = []
        for user in users:
            try:
                err, id = yield from self.post_user(user)
            except Exception as e:
                err = None, str(e)
            if err:
                user['err_msg'] = err[1]
                res['error'].append(user)
            else:
                user['id'] = id
                res['success'].append(user)
        return (None, res)
    
    def UploadFile(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int
        }, {
            'name': 'file',
        }, {
            'name': '+new_team',
            'type': bool,
        }, {
            'name': '+follow_rule',
            'type': bool
        }, {
            'name': '+password',
            'type': str,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        user = (yield self.db.execute('SELECT password FROM users WHERE id = %s;', (data['id'],))).fetchone()
        hpwd = HashPassword(data['password'])
        self.log(user)
        self.log(hpwd)
        if user['password'] != hpwd:
            return ((403, 'Confirm you password'), None)
        yield self.db.execute('UPDATE users SET follow_rule = %s, new_team = %s WHERE id = %s', (data['follow_rule'], data['new_team'], data['id']))
        folder = os.path.join(config.DATA_ROOT, 'data/users', str(data['id']))
        if data['file']:
            try: shutil.rmtree(folder)
            except: pass
            try: os.makedirs(folder)
            except: pass
            file_path = os.path.join(folder, data['file']['filename'])
            with open(file_path, 'wb+') as f:
                f.write(data['file']['body'])
        return (None, None)
