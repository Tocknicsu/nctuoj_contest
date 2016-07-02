from req import Service
from service.base import BaseService
from datetime import datetime
from datetime import timedelta


class Language(BaseService):
    def get_language_list(self):
        res = (yield self.db.execute("SELECT * FROM languages")).fetchall()
        return (None, res)

