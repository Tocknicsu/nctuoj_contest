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
from tornado_cors import CorsMixin

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

class RequestHandler(CorsMixin, tornado.web.RequestHandler):
    CORS_ORIGIN = '*'

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
        err, res = yield from Service.Util.contest_status()
        uri = self.request.uri.split('?')[0]
        if res == -1 and self.account['isADMIN'] == False and uri not in config.URL_WHITE_LIST:
            self.render((403, "Permission Denied"))
        now = Service.Permission
        for attr in self.path[1:]:
            if hasattr(now, attr):
                now = getattr(now, attr)
            else:
                return None
        method = self.request.method.lower()
        if not hasattr(now, method):
            return None
        res = getattr(now, method)(self, *self.path_args)
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
        
        if 'id' not in self.account:
            for x in map_users_type:
                self.account['is' + x] = False
            self.account['isLOGIN'] = False
            self.account['type'] = -1

        if token == config.JUDGE_TOKEN:
            self.account['isLOGIN'] = True
            self.account['isADMIN'] = True
            self.account['isJUDGE'] = True

class ApiRequestHandler(RequestHandler):
    def render(self, msg=""):
        # self.set_header('Access-Control-Allow-Origin', '*')
        if isinstance(msg, tuple): code, msg = msg
        else: code = 200
        self.set_status(code)
        try:
            msg = json.dumps({
                    'msg': msg
                }, cls=DatetimeEncoder)
        except:
            msg = str(msg)
        self.finish(msg)

    def write_error(self, err, **kwargs):
        self.render((err, kwargs))

    @tornado.gen.coroutine
    def prepare(self):
        res = yield super().prepare()
        ##################################################
        ### Check Permission                           ###
        ##################################################
        msg = yield self.check_permission()
        if isinstance(msg, tuple):
            self.render(msg)


class StaticFileHandler(tornado.web.StaticFileHandler, RequestHandler):
    @tornado.gen.coroutine
    def prepare(self):
        res = yield super().prepare()
        msg = yield self.check_permission()
        if isinstance(msg, tuple):
            self.set_status(msg[0])
            self.finish()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

