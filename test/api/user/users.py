data = [
    {
        "name": "test_get_users",
        "url": "/api/users/",
        "method": "get",
        "payload": {
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_get_users_admin",
        "url": "/api/users/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": [{
                "name": "admin", 
                "type": 0, 
                "password": "00b93578e0284e8a4b92fec5f386cbb5", 
                "id": 1, 
                "account": "admin", 
                "token": "ADMIN@TOKEN"
            }, {
                "name": "test", 
                "type": 1, 
                "password": "1dfb827eee41585df6d883ecffc2977a", 
                "id": 2, 
                "account": "test", 
                "token": "TEST@TOKEN"
            }, {
                "name": "unofficial", 
                "type": 2, 
                "password": "34ac961dc46e7be7bf46937a7f02f00d", 
                "id": 3, 
                "account": "unofficial", 
                "token": "UNOFFICIAL@TOKEN"
            }, {
                "name": "official", 
                "type": 3, 
                "password": "194d8a3231a17c7b6c72407f9c1d0930", 
                "id": 4, 
                "account": "official", 
                "token": "OFFICIAL@TOKEN"
            }] 
        }
    },
    {
        "name": "test_gen_user",
        "url": "/api/users/csv/",
        "method": "post",
        "payload": {
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_gen_user",
        "url": "/api/users/csv/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "files": {
            "users_file": "./api/user/users.csv"
        },
        "ignore": ["password", "repassword", "token", "err_msg"],
        "response_status": 200,
        "response_data": {
            "msg": {
                "error": [{
                    "name": "a", 
                    "account": "a",
                    "type": 1
                }, {
                    "account": "e", 
                    "name": "e", 
                    "type": 4
                }], 
                "success": [{
                    "account": "a", 
                    "name": "a", 
                    "id": 5, 
                    "type": 0
                }, {
                    "account": "b", 
                    "name": "b", 
                    "id": 6, 
                    "type": 1
                }, {
                    "account": "c", 
                    "name": "c", 
                    "id": 7, 
                    "type": 2
                }, {
                    "account": "d", 
                    "name": "d", 
                    "id": 8, 
                    "type": 3
                }]
            }
        }
    }
]
