from req import Service
from service.base import BaseService
import config
import os
import re


class Judge(BaseService):
    def get_submission(self):
        #res = yield self.db.execute("DELETE FROM wait_submissions WHERE id IN (SELECT id FROM wait_submissions ORDER BY id LIMIT 1) RETURNING submission_id")
        res = yield self.db.execute("SELECT submission_id FROM wait_submissions LIMIT 1");
        res = res.fetchone()
        return (None, res)
