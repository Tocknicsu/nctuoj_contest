data = [
    {
        "name": "test_get_contest",
        "url": "/api/contest/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": {"end": "2000-01-01 00:00:00", "start": "2000-01-01 00:00:00", "title": "NCTUOJ", "description": "Welcome to use NCTUOJ contest version. If you have any problem, please mailto wingemerald@gmail.com and allencat850502@gmail.com", "freeze": 0}
        }
    },
    {
        "name": "test_put_contest",
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
        "name": "test_put_contest_admin",
        "url": "/api/contest/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "title": "change",
            "start": "2001-01-01 00:00:00",
            "end": "2001-01-01 00:00:00",
            "freeze": "0",
            "description": "XD"
        }, 
        "response_status": 200,
        "response_data":{
            "msg": {"updated_at": "2016-06-24 18:49:33", "description": "XD", "created_at": "2016-06-24 18:49:30", "end": "2001-01-01 00:00:00", "start": "2001-01-01 00:00:00", "title": "change", "freeze": 0}
        }
    }
]
