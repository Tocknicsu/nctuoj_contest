data = [
    {
        "name": "test_post_problem",
        "url": "/api/problems/",
        "method": "post",
        "payload": {
            "title": "problem A",
            "score_type": 0
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    }, 
    {
        "name": "test_post_problem_admin",
        "url": "/api/problems/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
            "title": "problem A",
            "score_type": 0
        },
        "files": {
            "pdf": "./api/problem/problem.pdf"
        },
        "response_status": 200,
        "response_data": {
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "testdata": [], "executes": [], "verdict": {"execute_type_id": 2, "id": 1, "file_name": "main.cpp"}}
        }
    },
    {
        "name": "test_put_problem_execute",
        "url": "/api/problems/1/executes/",
        "method": "put",
        "payload": {
            "executes[]": [1, 2, 3, 4]
        },
        "response_status": 403,
        "response_data": {
            "msg": "Permission Denied"
        }
    },
    {
        "name": "test_put_problem_execute_admin",
        "url": "/api/problems/1/executes/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "executes[]": [1, 2, 3, 4]
        },
        "response_status": 200,
        "response_data": {
            "msg": [{"description": "C", "id": 1}, {"description": "C++11", "id": 2}, {"description": "C++14", "id": 3}, {"description": "Java", "id": 4}]
        }
    },
    {
        "name": "test_put_problem_execute_no_exist",
        "url": "/api/problems/2/executes/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "executes[]": [1, 2, 3, 4]
        },
        "response_status": 404,
        "response_data": {
            "msg": "Not Found"
        }
    }
]
