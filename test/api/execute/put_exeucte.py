data = [
    {
        "name": "test_put_execute_no_login",
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
        "name": "test_put_execute_test",
        "url": "/api/executes/1/",
        "method": "put",
        "payload": {
            "token": "TEST@TOKEN",
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
        "name": "test_put_execute_unofficial",
        "url": "/api/executes/1/",
        "method": "put",
        "payload": {
            "token": "UNOFFICIAL@TOKEN",
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
        "name": "test_put_execute_official",
        "url": "/api/executes/1/",
        "method": "put",
        "payload": {
            "token": "OFFICIAL@TOKEN",
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
        "name": "test_put_execute_admin_no_exist",
        "url": "/api/executes/999/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "description": "C",
            "commands[]": ["gcc -lm -std=c99 __FILE__", "./a.out"],
            "file_name": "main.c",
        },
        "response_status": 404,
        "response_data": {
            "msg": "Not Found"
        }
    },
]
