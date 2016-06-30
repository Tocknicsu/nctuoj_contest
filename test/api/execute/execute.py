data = [
    {
        "name": "test_get_execute",
        "url": "/api/executes/1/",
        "method": "get",
        "payload": {
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "id": 1,
                "description": "C",
                "commands": [{"command": "gcc -lm -std=c99 __FILE__"}, {"command": "./a.out"}],
                "file_name": "main.c"
            }
        }
    },
    {
        "name": "test_get_execute_no_exist",
        "url": "/api/executes/100/",
        "method": "get",
        "payload": {
        },
        "response_status": 404,
        "response_data": {
            "msg": "Not Found"
        }
    },
    {
        "name": "test_put_execute",
        "url": "/api/executes/1/",
        "method": "put",
        "payload": {
            "description": "C",
            "commands[]": ["gcc -lm -std=c99 __FILE__", "./a.out"],
            "file_name": "main.c",
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_put_execute_admin",
        "url": "/api/executes/1/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "description": "C",
            "commands[]": ["gcc -lm -std=c99 __FILE__", "./a.out"],
            "file_name": "main.c",
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "id": 1,
                "description": "C",
                "commands": [{"command": "gcc -lm -std=c99 __FILE__"}, {"command": "./a.out"}],
                "file_name": "main.c"
            }
        }
    },
    {
        "name": "test_delete_execute",
        "url": "/api/executes/1/",
        "method": "delete",
        "payload": {
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_delete_execute_admin",
        "url": "/api/executes/1/",
        "method": "delete",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "id": 1
            }
        }
    }
]