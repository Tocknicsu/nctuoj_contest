import json
import datetime
import tornado.template
import tornado.gen
import tornado.web
import tornado.websocket
import datetime
from urllib.parse import quote
from log import log
import momoko
import config
import types
from utils.form import form_validation
from utils.utils import *
from include import *
from map import *

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class Service:
    pass

def Service__init__():
    ##################################################
    ### Setting db                                 ###
    ##################################################
    db = momoko.Pool(**config.DB_SETTING)
    future = db.connect()
    tornado.ioloop.IOLoop.instance().add_future(future, lambda f: tornado.ioloop.IOLoop.instance().stop())
    tornado.ioloop.IOLoop.instance().start()
    ##################################################
    ### Setting Service                            ###
    ##################################################
    Service.db = db
    Service.log = log
    Service.form_validation = form_validation
    ##################################################
    ### Importing Service Module                   ###
    ##################################################
    include(Service, "./service", ["base.py"], True)
    Service.Permission = T()
    include(Service.Permission, "./permission/", ["base.py"], True)

class RequestHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = log


    def get_args(self, name):
        meta = {}
        for n in name:
            try:
                if n[-2:] == "[]":
                    meta[n[:-2]] = self.get_arguments(n)
                elif n[-6:] == "[file]":
                    n = n[:-6]
                    meta[n] = self.request.files[n][0]
                else:
                    meta[n] = self.get_argument(n)
            except:
                meta[n] = None
        return meta

    @tornado.gen.coroutine
    def check_permission(self):
        now = Service.Permission
        for attr in self.path[1:]:
            if hasattr(now, attr):
                now = getattr(now, attr)
            else:
                return None
        method = self.request.method.lower()
        if not hasattr(now, method):
            return None
        res = getattr(now, method)(self)
        if isinstance(res, types.GeneratorType):
            res = yield from res
        return res


    @tornado.gen.coroutine
    def prepare(self):
        ##################################################
        ### Get IP                                     ###
        ##################################################
        x_real_ip = self.request.headers.get("X-Real-IP")
        remote_ip = x_real_ip or self.request.remote_ip
        self.remote_ip = remote_ip
        self.log("[%s] %s %s"%(self.request.method, self.request.uri, self.remote_ip))


        yield self.get_identity()
        ##################################################
        ### Get Identity                               ###
        ##################################################
        ### API Using token
        ##################################################
        ### Get Basic Information                      ###
        ##################################################
       
        ##################################################
        ### Check Permission                           ###
        ##################################################
        err = yield self.check_permission()
        if err:
            self.write_error((403, err))
        


class ApiRequestHandler(RequestHandler):
    def render(self, msg=""):
        if isinstance(msg, tuple): code, msg = msg
        else: code = 200
        self.set_status(code)
        self.finish(json.dumps({
                'msg': msg
            },
            cls=DatetimeEncoder))

    def write_error(self, err, **kwargs):
        self.render(err)

    @tornado.gen.coroutine
    def prepare(self):
        res = yield super().prepare()

    @tornado.gen.coroutine
    def get_identity(self):
        token = self.get_args(['token'])['token']
        if token:
            err, res = yield from Service.User.get_user_by_token({'token': token})
            if err:
                self.account = {}
            else:
                self.account = res
        else:
            self.account = {}
        self.account['isLOGIN'] = False
        for x in map_users_type:
            self.account['is'+x] = 'type' in self.account and self.account['type'] == map_users_type[x]
            self.account['isLOGIN'] = self.account['isLOGIN'] or self.account['is'+x]


class StaticFileHandler(tornado.web.StaticFileHandler):
    def prepare(self):
        super().prepare()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

