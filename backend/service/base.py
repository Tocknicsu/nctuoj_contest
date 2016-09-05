from copy import copy
from utils.log import log
from req import Service

class BaseService:
    def __init__(self):
        self.db = Service.db
        self.form_validation = Service.form_validation
        self.log = Service.log

    def gen_insert_sql(self, tablename, _data):
        data = copy(_data)
        for col in _data:
            if _data[col] is None:
                del data[col]
        sql1 = ''.join( ' "%s",'%col for col in data )[:-1]
        sql2 = (' %s,'*len(data))[:-1]
        param = tuple( val for val in data.values() )
        sql = 'INSERT INTO "%s" (%s) VALUES(%s) RETURNING id;' % (tablename, sql1, sql2)
        return (sql, param)
    
    def gen_update_sql(self, tablename, _data):
        data = copy(_data)
        for col in _data:
            if _data[col] is None:
                del data[col]
        sql = ''.join(' "%s" = %%s,'%col for col in data)[:-1]
        param = tuple( val for val in data.values() )
        sql = 'UPDATE "%s" SET %s '%(tablename, sql)
        return (sql, param)

    def gen_select_sql(self, tablename, data):
        sql = ''.join(' "%s",'%col for col in data)[:-1]
        sql = 'SELECT %s FROM "%s" '%(sql, tablename)
        return sql
    
    def calc_limit_offset(self, page, count):
        page = int(page)
        count = int(count)
        offset = (page - 1) * count
        return (count, offset)

