from req import Service
from permission.base import BasePermission


class Scoreboard(BasePermission):
    def put(self, req):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")

