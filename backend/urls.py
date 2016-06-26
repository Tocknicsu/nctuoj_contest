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
    ('/api/problems/(\d+)/', Handler.api.Problem),
    ('/api/Problems/(\d+)/executes/', Handler.api.ProblemExecutes),
    ('/api/clarifications/', Handler.api.Clarifications),
    ('/api/clarifications/(\d+)/', Handler.api.Clarification),
    ('/api/executes/', Handler.api.Executes),
    ('/api/executes/(\d+)/', Handler.api.Execute),
    ('/api/system/(\w*)/', Handler.api.System),
]
