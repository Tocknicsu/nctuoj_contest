from include import include
class Handler:
    pass
include(Handler, "./handler/")
urls = [
    ('/', Handler.Index),
    ('/api/simple/', Handler.api.Simple),
]
