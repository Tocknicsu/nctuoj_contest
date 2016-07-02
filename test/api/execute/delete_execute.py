data = [
    {
        "name": "test_delete_execute_no_login",
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
        "name": "test_delete_execute_test",
        "url": "/api/executes/1/",
        "method": "delete",
        "payload": {
            "token": "TEST@TOKEN"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_delete_execute_unofficial",
        "url": "/api/executes/1/",
        "method": "delete",
        "payload": {
            "token": "UNOFFICIAL@TOKEN"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_delete_execute_official",
        "url": "/api/executes/1/",
        "method": "delete",
        "payload": {
            "token": "OFFICIAL@TOKEN"
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
    },
    {
        "name": "test_delete_execute_admin_no_exist",
        "url": "/api/executes/1/",
        "method": "delete",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 404,
        "response_data": {
            "msg": "Not Found"
        }
    }
]
