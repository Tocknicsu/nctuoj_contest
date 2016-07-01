data = [
    {
        "name": "post_problem",
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
            "msg": {"id": 1, "score_type": 0, "title": "problem A", "executes": [], "testdata": [], "verdict": {"execute_type_id": 2, "id": 1, "file_name": "main.cpp"}}
        }
    },
    {
        "name": "put_problem_execute",
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
        "name": "post_testdata",
        "url": "/api/problems/1/testdata/",
        "method": "post",
        "files": {
            "input": "./api/testdata/1.in",
            "output": "./api/testdata/1.out"
        },
        "payload": {
            "token": "ADMIN@TOKEN",
            "score": 100,
            "memory_limit": 65536,
            "time_limit": 1000,
            "output_limit": 64
        },
        "response_status": 200,
        "response_data":{
            "msg": {"output_limit": 64, "updated_at": "2016-06-27 14:55:36", "time_limit": 1000, "created_at": "2016-06-27 14:55:36", "id": 1, "memory_limit": 65536, "problem_id": 1, "score": 100}
        }
    },
    {
        "name": "post_testdata",
        "url": "/api/problems/1/testdata/",
        "method": "post",
        "files": {
            "input": "./api/testdata/2.in",
            "output": "./api/testdata/2.out"
        },
        "payload": {
            "token": "ADMIN@TOKEN",
            "score": 100,
            "memory_limit": 65536,
            "time_limit": 1000,
            "output_limit": 64
        },
        "response_status": 200,
        "response_data":{
            "msg": {"output_limit": 64, "updated_at": "2016-06-27 14:54:39", "time_limit": 1000, "created_at": "2016-06-27 14:54:39", "id": 2, "memory_limit": 65536, "problem_id": 1, "score": 100}
        }
    },
    {
        "name": "get_testdata",
        "url": "/api/problems/1/testdata/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": [{"memory_limit": 65536, "problem_id": 1, "time_limit": 1000, "id": 1, "output_limit": 64, "created_at": "2016-06-27 14:40:06", "updated_at": "2016-06-27 14:40:06", "score": 100}, {"memory_limit": 65536, "problem_id": 1, "time_limit": 1000, "id": 2, "output_limit": 64, "created_at": "2016-06-27 14:40:06", "updated_at": "2016-06-27 14:40:06", "score": 100}]
        }
    },
    {
        "name": "get_testdatum",
        "url": "/api/problems/1/testdata/1/",
        "method": "get",
        "payload": {
            "token": "ADMIN@TOKEN"
        },
        "response_status": 200,
        "response_data": {
            "msg": {"id": 1, "score": 100, "time_limit": 1000, "memory_limit": 65536, "output_limit": 64, "problem_id": 1, "updated_at": "2016-06-27 14:46:49", "created_at": "2016-06-27 14:46:49"}
        }
    }
]
