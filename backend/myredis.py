import redis
import pickle
import config

class MyRedis(redis.StrictRedis):
    def __init__(self, host='localhost', port=6379, db=0, data_expire_second=3600):
        super().__init__(host=host, port=port, db=db)
        self.data_expire_second = data_expire_second

    def set(self, name, value, time=None):
        return self.setex(name, time or self.data_expire_second, value)

    def get(self, name):
        res = super().get(name)
        if not res:
            return None
        return pickle.loads(res, encoding='utf-8')

    def setex(self, name, time, value):
        value = pickle.dumps(value)
        return super().setex(name, time, value)

    def setnx(self, name, value):
        value = pickle.dumps(value)
        return super().setnx(name, value)

    def getset(self, name, value):
        value = pickle.dumps(value)
        return pickle.loads(super().getset(name, value), encoding='utf-8')

