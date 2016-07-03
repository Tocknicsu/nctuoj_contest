from req import Service
from permission.base import BasePermission


class JudgeSubmission(BasePermission):
    def get(self, req):
        if 'isJUDGE' not in req.account or not req.account['isJUDGE']:
            return (403, "Permission Denied")

