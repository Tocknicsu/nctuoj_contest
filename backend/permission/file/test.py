from req import Service
from permission.base import BasePermission

class Test(BasePermission):
    def get(self, req, id):
        if not req.account['isLOGIN']:
            return (403, 'Permission Denied')

