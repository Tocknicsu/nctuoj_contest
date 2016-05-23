#!/usr/bin/env python3
import sys
import requests
import json
import unittest
import datetime
from util import TestCase
import config

class TestApiUserSignin(TestCase):
    url = "%s/api/users/signin/"%(config.base_url,)

    def test_login(self):
        data = {
            "account": config.user_admin_account,
            "password": config.user_admin_password,
        }
        res = requests.post(self.url, data=data)
        res.connection.close()
        expect_result = {
            "status_code": 200,
            "body": {
                "msg": config.user_admin_token,
            }
        }
        self.assertEqualR(res, expect_result)
    
    def test_login_failed(self):
        data = {
            "account": config.user_admin_account,
            "password": config.user_admin_password + str(datetime.datetime.now()),
        }
        res = requests.post(self.url, data=data)
        res.connection.close()
        expect_result = {
            "status_code": 403,
            "body": {
                "msg": "Wrong Password",
            }
        }
        self.assertEqualR(res, expect_result)

    def test_login_no_user(self):
        data = {
            "account": config.user_admin_account + str(datetime.datetime.now()),
            "password": config.user_admin_password + str(datetime.datetime.now()),
        }
        res = requests.post(self.url, data=data)
        res.connection.close()
        expect_result = {
            "status_code": 404,
            "body": {
                "msg": "User Not Exist",
            }
        }
        self.assertEqualR(res, expect_result)

