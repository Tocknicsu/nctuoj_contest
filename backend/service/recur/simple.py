from req import Service
from service.base import BaseService

class Simple(BaseService):
    def get_simple(self):
        second = 1
        res = yield self.db.execute('SELECT PG_SLEEP(%s);', (second,))
        self.log("Service log Test")
        return (None, 'you slept %s seconds'%(second))

    def post_simple(self, data={}):
        required_args = [{
            'name': '+a',
            'type': int,
        }, {
            'name': '+b',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute('SELECT %s+%s AS sum;', (data['a'], data['b'], ))
        return (None, res.fetchone()['sum'])

class simple2(BaseService):
    def get_simple(self):
        print("OK")
        return (None, 'you slept %s seconds'%(0))
