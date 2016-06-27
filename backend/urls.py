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
    ('/api/problems/(\d+)/executes/', Handler.api.ProblemExecutes),
    #('/api/problems/(\d+)/rejudge/', Handler.api.ProblemRejudge),
    #('/api/problems/(\d+)/testdata/', Handler.api.ProblemTestdata),
    ('/api/submissions/', Handler.api.Submissions),
    #('/api/submissions/(\d+)/', Handler.api.Submission),
    #('/api/submissions/(\d+)/rejudge/', Handler.api.SubmissionRejudge),
    ('/api/clarifications/', Handler.api.Clarifications),
    ('/api/clarifications/(\d+)/', Handler.api.Clarification),
    ('/api/executes/', Handler.api.Executes),
    ('/api/executes/(\d+)/', Handler.api.Execute),
    ('/api/system/(\w*)/', Handler.api.System),
]
