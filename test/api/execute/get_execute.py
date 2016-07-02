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
]
