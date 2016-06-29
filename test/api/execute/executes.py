data = [
    {
        "name": "test_get_executes",
        "url": "/api/executes/",
        "method": "get",
        "payload": {
        },
        "response_status": 200,
        "response_data": {
            "msg": [
                {"id": 1, "description": "C", "file_name": "main.c"}, 
                {"id": 2, "description": "C++11", "file_name": "main.cpp"},
                {"id": 3, "description": "C++14", "file_name": "main.cpp"}, 
                {"id": 4, "description": "Java", "file_name": "Main.java"}, 
                {"id": 5, "description": "Python2", "file_name": "main.py"}, 
                {"id": 6, "description": "Python3", "file_name": "main.py"},
            ]
        }
    },
    {
        "name": "test_post_executes",
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
        "name": "test_post_executes_admin",
        "url": "/api/executes/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
            "description": "NEW",
            "commands[]": ["NEW COMMAND1", "NEW COMMAND2"],
            "file_name": "default.filename"
        },
        "response_status": 200,
        "response_data": {
            "msg": {
                "commands": [{"command": "NEW COMMAND1"}, {"command": "NEW COMMAND2"}], 
                "description": "NEW", 
                "id": 7,
                "file_name": "default.filename",
            }
        }
    }
]
