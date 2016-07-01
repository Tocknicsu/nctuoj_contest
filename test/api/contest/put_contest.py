import datetime
data = [
    {
        "name": "test_put_contest_no_login",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "title": "change",
            "start": "2001-01-01 00:00:00",
            "end": "2001-01-01 00:00:00",
            "freeze": "0",
            "description": "XD"
        }, 
        "response_status": 403,
        "response_data":{
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_put_contest_test",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "TEST@TOKEN",
            "title": "change",
            "start": "2001-01-01 00:00:00",
            "end": "2001-01-01 00:00:00",
            "freeze": "0",
            "description": "XD"
        }, 
        "response_status": 403,
        "response_data":{
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_put_contest_unofficial",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "UNOFFICIAL@TOKEN",
            "title": "change",
            "start": "2001-01-01 00:00:00",
            "end": "2001-01-01 00:00:00",
            "freeze": "0",
            "description": "XD"
        }, 
        "response_status": 403,
        "response_data":{
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_put_contest_official",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "OFFICIAL@TOKEN",
            "title": "change",
            "start": "2001-01-01 00:00:00",
            "end": "2001-01-01 00:00:00",
            "freeze": "0",
            "description": "XD"
        }, 
        "response_status": 403,
        "response_data":{
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_put_contest_admin",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "title": "change",
            "start": str(datetime.datetime.now())[:-7],
            "end": str(datetime.datetime.now() + datetime.timedelta(hours=3))[:-7],
            "freeze": 0,
            "description": "XD"
        }, 
        "response_status": 200,
        "response_data":{
            "msg": {
                "title": "change",
                "start": str(datetime.datetime.now())[:-7],
                "end": str(datetime.datetime.now() + datetime.timedelta(hours=3))[:-7],
                "freeze": 0,
                "description": "XD"
            }
        }
    },
    {
        "name": "test_put_contest_admin_wrong_time(start > end)",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "title": "change",
            "start": str(datetime.datetime.now())[:-7],
            "end": str(datetime.datetime.now() + datetime.timedelta(hours=-3))[:-7],
            "freeze": 0,
            "description": "XD"
        }, 
        "response_status": 400,
        "response_data":{
            "msg": "start cannot larger than end"
        }
    },
    {
        "name": "test_put_contest_admin_wrong_time(start + freeze > end)",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "title": "change",
            "start": str(datetime.datetime.now())[:-7],
            "end": str(datetime.datetime.now() + datetime.timedelta(hours=3))[:-7],
            "freeze": 200,
            "description": "XD"
        }, 
        "response_status": 400,
        "response_data":{
            "msg": "start + freeze cannot larger than end"
        }
    }

]
