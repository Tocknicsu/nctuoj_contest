data = [
    {
        "name": "test_post_executes_no_login",
        "url": "/api/executes/",
        "method": "post",
        "payload": {
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_post_executes_test",
        "url": "/api/executes/",
        "method": "post",
        "payload": {
            "token": "TEST@TOKEN",
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_post_executes_unofficial",
        "url": "/api/executes/",
        "method": "post",
        "payload": {
            "token": "UNOFFICIAL@TOKEN",
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_post_executes_official",
        "url": "/api/executes/",
        "method": "post",
        "payload": {
            "token": "OFFICIAL@TOKEN",
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_post_executes_admin",
        "url": "/api/executes/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
            "description": "NEW",
            "commands[]": ["NEW COMMAND1", "NEW COMMAND2"],
            "file_name": "default.filename",
            "language_id": 1,
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "commands": [{"command": "NEW COMMAND1"}, {"command": "NEW COMMAND2"}], 
                "description": "NEW", 
                "id": 7,
                "file_name": "default.filename",
                "language_id": 1,
            }
        }
    }
]
