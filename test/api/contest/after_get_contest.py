import datetime
start = datetime.datetime.now() + datetime.timedelta(hours=-4)
end = datetime.datetime.now() + datetime.timedelta(hours=-1)
start = str(start)[:-7]
end = str(end)[:-7]
data = [
    {
        "name": "adjust to now is before contest",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "title": "change",
            "start": start,
            "end": end,
            "freeze": 0,
            "description": "XD"
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "title": "change",
                "start": start,
                "end": end,
                "freeze": 0,
                "description": "XD"
            }
        }
    },
    {
        "name": "test_get_contest_no_login",
        "url": "/api/contest/",
        "method": "get",
        "payload": {
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "title": "change",
                "start": start,
                "end": end,
                "freeze": 0,
                "description": "XD"
            }
        }
    },
    {
        "name": "test_get_contest_test",
        "url": "/api/contest/",
        "method": "get",
        "payload": {
            "token": "TEST@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "title": "change",
                "start": start,
                "end": end,
                "freeze": 0,
                "description": "XD"
            }
        }
    },
    {
        "name": "test_get_contest_unofficail",
        "url": "/api/contest/",
        "method": "get",
        "payload": {
            "token": "UNOFFICIAL@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "title": "change",
                "start": start,
                "end": end,
                "freeze": 0,
                "description": "XD"
            }
        }
    },
    {
        "name": "test_get_contest_officail",
        "url": "/api/contest/",
        "method": "get",
        "payload": {
            "token": "OFFICIAL@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "title": "change",
                "start": start,
                "end": end,
                "freeze": 0,
                "description": "XD"
            }
        }
    },
    {
        "name": "test_get_contest_admin",
        "url": "/api/contest/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "title": "change",
                "start": start,
                "end": end,
                "freeze": 0,
                "description": "XD"
            }
        }
    },
]
