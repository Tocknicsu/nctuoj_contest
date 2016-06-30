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
    #('/api/problems/meta/', Handler.api.ProblemsMeta),
    ('/api/problems/(\d+)/', Handler.api.Problem),
    #('/api/problems/(\d+)/', Handler.api.ProblemMeta),
    ('/api/problems/(\d+)/executes/', Handler.api.ProblemExecutes),
    #('/api/problems/(\d+)/rejudge/', Handler.api.ProblemRejudge),
    ('/api/problems/(\d+)/testdata/', Handler.api.Testdata),
    ('/api/problems/(\d+)/testdata/(\d+)/', Handler.api.Testdatum),
    #('/api/problems/(\d+)/testdata/(\d+)/(\w*)/', Handler.api.TestdatumFile),
    ('/api/submissions/', Handler.api.Submissions),
    ('/api/submissions/(\d+)/', Handler.api.Submission),
    #('/api/submissions/(\d+)/rejudge/', Handler.api.SubmissionRejudge),
    ('/api/clarifications/', Handler.api.Clarifications),
    ('/api/clarifications/(\d+)/', Handler.api.Clarification),
    ('/api/executes/', Handler.api.Executes),
    ('/api/executes/(\d+)/', Handler.api.Execute),
    ('/api/verdicts/', Handler.api.Verdicts),
    ('/api/system/(\w*)/', Handler.api.System),
    ('/api/scoreboard/', Handler.api.Scoreboard),
    ('/file/test/(\w*)', Handler.file.Test, {'path': '/tmp/'}),
]
