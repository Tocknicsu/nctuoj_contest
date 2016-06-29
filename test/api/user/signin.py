data = [
    {
        "name": "test_signin",
        "url": "/api/users/signin/",
        "method": "post",
        "payload": {
            "account": "admin",
            "password": "admin"
        },
        "response_status": 200,
        "response_data": {
            "msg": {"isADMIN": True, "isLOGIN": True, "account": "admin", "isOFFICIAL": False, "isUNOFFICIAL": False, "token": "ADMIN@TOKEN", "isTEST": False, "name": "admin", "id": 1, "type": 0, "updated_at": "2016-06-29 19:11:19", "created_at": "2016-06-29 19:11:19"}
        }
    },
    {
        "name": "test_signin_failed",
        "url": "/api/users/signin/",
        "method": "post",
        "payload": {
            "account": "admin",
            "password": "adminwrongpassword"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Wrong Password"
        }
    },
    {
        "name": "test_signin_no_user",
        "url": "/api/users/signin/",
        "method": "post",
        "payload": {
            "account": "admin1245",
            "password": "admin"
        },
        "response_status": 404,
        "response_data": {
            "msg": "User Not Exist"
        }
    }
]
