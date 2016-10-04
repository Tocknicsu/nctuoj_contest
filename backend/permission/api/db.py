from req import Service
from permission.base import BasePermission

class DB(BasePermission):
    def delete(self, req, name):
        if not req.account['isADMIN']:
            return (403, "Permission Denied")
