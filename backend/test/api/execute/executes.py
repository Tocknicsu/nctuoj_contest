#!/usr/bin/env python3
import sys
import requests
import json
import unittest
import datetime
from util import TestCase
import config

class TestApiExecutes(TestCase):
    url = "%s/api/executes/"%(config.base_url,)

    def test_get(self):
        res = requests.get(self.url)
        res.connection.close()
        expect_result = {
            "status_code": 200,
            "body": {
                "msg": [{"id": 1, "description": "C", "priority": 1}, {"id": 2, "description": "C++", "priority": 2}, {"id": 3, "description": "C++11", "priority": 3}, {"id": 4, "description": "Java", "priority": 4}]
            }
        }
        self.assertEqualR(res, expect_result)


    
