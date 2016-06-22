from include import include
class Handler:
    pass
include(Handler, "./handler/")
urls = [
    ('/', Handler.Index),
    ('/api/contest/', Handler.api.Contest),
    ('/api/users/', Handler.api.Users),
    ('/api/users/me/', Handler.api.UsersMe),
    ('/api/users/csv/', Handler.api.UsersCSV),
    ('/api/users/signin/', Handler.api.UserSignIn),
    ('/api/problems/', Handler.api.Problems),
    ('/api/problem/', Handler.api.Problem),
    ('/api/clarifications/', Handler.api.Clarifications),
    ('/api/clarification/(\d+)/', Handler.api.Clarification),
    ('/api/executes/', Handler.api.Executes),
    ('/api/executes/(\d+)/', Handler.api.Execute),
    ('/api/system/(\w*)/', Handler.api.System),
]
