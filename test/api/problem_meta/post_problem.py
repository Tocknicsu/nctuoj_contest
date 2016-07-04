data = [
    {
        "name": "test_post_problem_admin(missing meta.json)",
        "url": "/api/problems/meta/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/problem_meta/missing_meta.zip"
        },
        "response_status": 400,
        "response_data": {
            "msg": "meta.json not in the zip"
        }
    }, 
    {
        "name": "test_post_problem_admin",
        "url": "/api/problems/meta/",
        "method": "post",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/problem_meta/problem_meta.zip"
        },
        "response_status": 200,
        "response_data": {
            "msg": {"executes": [{"description": "C", "id": 1}, {"description": "C++11", "id": 2}, {"description": "C++14", "id": 3}, {"description": "Java", "id": 4}], "score_type": 1, "verdict": {"file_name": "main.cpp", "id": 1, "execute_type_id": 2}, "testdata": [{"output_limit": 64, "time_limit": 1000, "memory_limit": 65536, "id": 1, "score": 100, "problem_id": 1}, {"output_limit": 64, "time_limit": 1000, "memory_limit": 65536, "id": 2, "score": 100, "problem_id": 1}], "title": "Problem A", "id": 1}
        }
    }, 
    {
        "name": "test_put_problem_admin(missing meta.json)",
        "url": "/api/problems/1/meta/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/problem_meta/missing_meta.zip"
        },
        "response_status": 400,
        "response_data": {
            "msg": "meta.json not in the zip"
        }
    }, 
    {
        "name": "test_put_problem_admin",
        "url": "/api/problems/1/meta/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
        },
        "files": {
            "zip": "./api/problem_meta/problem_meta.zip"
        },
        "response_status": 200,
        "response_data": {
            "msg": {"executes": [{"description": "C", "id": 1}, {"description": "C++11", "id": 2}, {"description": "C++14", "id": 3}, {"description": "Java", "id": 4}], "score_type": 1, "verdict": {"file_name": "main.cpp", "execute_type_id": 2, "id": 1}, "testdata": [{"output_limit": 64, "time_limit": 1000, "memory_limit": 65536, "id": 3, "score": 100, "problem_id": 1}, {"output_limit": 64, "time_limit": 1000, "memory_limit": 65536, "id": 4, "score": 100, "problem_id": 1}], "title": "Problem A", "id": 1}
        }
    }, 
]
