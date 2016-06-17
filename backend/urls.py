from include import include
class Handler:
    pass
include(Handler, "./handler/")
urls = [
    ('/', Handler.Index),
    ('/api/users/gen/', Handler.api.UsersGen),
    ('/api/users/signin/', Handler.api.UserSignIn),
    ('/api/executes/', Handler.api.Executes),
    ('/api/executes/(\d+)/', Handler.api.Execute),
]
