data = [
    {
        "name": "test_get_users",
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
                "id": 1, 
                "account": "admin", 
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
        "ignore": ["password", "repassword", "token", "err_msg", "id"],
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
