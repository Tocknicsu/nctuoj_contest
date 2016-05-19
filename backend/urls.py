from include import include
class Handler:
    pass
include(Handler, "./handler/")
urls = [
    ('/api/simple/', Handler.api.Simple),
    ('/api/recur/simple/', Handler.api.recur.Simple),
]
