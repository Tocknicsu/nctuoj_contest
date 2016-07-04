from req import Service
from req import DatetimeEncoder
from service.base import BaseService
from datetime import datetime
import json


class Scoreboard(BaseService):
    def get_scoreboard(self, data={}):
        required_args = [{
            'name': '+type',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = (yield self.db.execute("SELECT * FROM scoreboard WHERE id=%s", (data['type'],))).fetchone()
        self.log(res)
        return (None, res)

    def put_scoreboard(self, data={}):
        VERDICT_AC = 10
        required_args = [{
            'name': '+type',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err:
            return (rer, None)
        err, contest = yield from Service.Contest.get_contest()
        err, users = yield from Service.User.get_user_list({'account': {'type': data['type']}})
        users = dict({x['id']: x for x in users})
        err, problems = yield from Service.Problem.get_problem_list()
        problems = dict({x['id']: x for x in problems})
        for user_id in users:
            users[user_id]['problems'] = {}
            for problem_id in problems:
                users[user_id]['problems'][problem_id] = {
                            'verdict_id': 0, 
                            'penalty': 0,
                            'attempt': 0,
                            'ac_time': None,
                        }
        for problem_id in problems:
            problems[problem_id]['attempt'] = 0
            problems[problem_id]['ac'] = 0
        err, submissions = yield from Service.Submission.get_submission_list_admin({
                'count': (1 << 31) - 1,
                'page': 1,
            })
        submissions = submissions['data']
        self.log(submissions)
        # iterate submission list
        for submission in submissions:
            if submission['user_id'] not in users: # not in user list
                continue
            user_id = submission['user_id']
            problem_id = submission['problem_id']
            if users[user_id]['problems'][problem_id]['verdict_id'] == VERDICT_AC: # AC already
                continue
            if submission['verdict_id'] == VERDICT_AC:
                users[user_id]['problems'][problem_id]['ac_time'] = (submission['created_at'] - contest['start']) // 60
                problems[problem_id]['ac'] += 1
            users[user_id]['problems'][problem_id]['verdict_id'] = submission['verdict_id']
            users[user_id]['problems'][problem_id]['attempt'] += 1
            problems[problem_id]['attempt'] += 1
        # iterate user list to update user info
        for user_id in users:
            # remove personal info
            users[user_id].pop('token')
            users[user_id].pop('password')
            users[user_id]['attempt'] = 0
            users[user_id]['penalty'] = 0
            users[user_id]['ac'] = 0
            for problem_id in users[user_id]['problems']:
                users[user_id]['attempt'] += users[user_id]['problems'][problem_id]['attempt']
                users[user_id]['penalty'] += users[user_id]['problems'][problem_id]['penalty']
                users[user_id]['ac'] += users[user_id]['problems'][problem_id]['verdict_id'] == VERDICT_AC
        users = list(users[x] for x in users)
        problems = list(problems[x] for x in problems)
        # sort
        users = sorted(users, key = lambda x: (-x['ac'], x['penalty']))
        now_rank = 0
        now_rank_idx = (1, 0)
        for user in users:
            self.log(now_rank_idx)
            self.log((-user['ac'], user['penalty']))
            if now_rank_idx != (-user['ac'], user['penalty']):
                now_rank += 1
                now_rank_idx = (-user['ac'], user['penalty'])
            user['rank'] = now_rank
        res = {}
        res['users'] = users
        res['problems'] = problems
        yield self.db.execute('UPDATE scoreboard SET data = %s WHERE id = %s;', (json.dumps(res, cls=DatetimeEncoder), data['type'],))
        return (None, res)
