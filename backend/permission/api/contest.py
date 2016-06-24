from req import Service
from permission.base import BasePermission


class Contest(BasePermission):
    def put(self, req):
        ### No Login
        if not req.account['isADMIN']:
            return (403, "Permission Denied")


