from req import Service
from permission.base import BasePermission


class UsersGen(BasePermission):
    def post(self, req):
        ### No Login
        if not req.isAdmin:
            return 403

        return None
