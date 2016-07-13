data = [
]

for i in range(0, 4):
    data.append({
        "name": "put_scoreboard",
        "url": "/api/scoreboard/",
        "method": "put",
        "payload": {
            "token": "ADMIN@TOKEN",
            "type": i
        },
        "ignore": ["msg",],
        "response_status": 200,
        "response_data": {
        }
    })
