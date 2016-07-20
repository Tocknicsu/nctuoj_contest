from req import Service
from permission.base import BasePermission


class Contest(BasePermission):
    def get(self, req):
        err, res = yield from Service.Util.contest_status()
        if res == -1 and self.account['isADMIN'] == False:
            return (403, "Permission Denied")

    def put(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
