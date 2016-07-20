from req import Service
from req import DatetimeEncoder
from service.base import BaseService
from datetime import datetime
from datetime import timedelta
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
        return (None, res)

    def put_scoreboard(self, data={}):
        VERDICT_AC = 10
        PENALTY = 20
        required_args = [{
            'name': '+type',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err:
            return (rer, None)
        err, contest = yield from Service.Contest.get_contest()
        err, users = yield from Service.User.get_user_list(data)
        users = dict({x['id']: x for x in users})
        err, problems = yield from Service.Problem.get_problem_list()
        problems = dict({x['id']: x for x in problems})
        for user_id in users:
            users[user_id]['problems'] = {}
            for problem_id in problems:
                users[user_id]['problems'][problem_id] = {
                            'id': problem_id,
                            'verdict_id': 0, 
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
        # iterate submission list
        for submission in reversed(submissions):
            if submission['user_id'] not in users: # not in user list
                continue
            user_id = submission['user_id']
            problem_id = submission['problem_id']
            if users[user_id]['problems'][problem_id]['verdict_id'] == VERDICT_AC: # AC already
                continue
            if submission['verdict_id'] > 2:
                users[user_id]['problems'][problem_id]['attempt'] += 1
                problems[problem_id]['attempt'] += 1
            if data['type'] != 0: # not admin
                if contest['freeze'] < 0:
                    if submission['created_at'] > contest['end'] + timedelta(minutes=contest['freeze']):
                        continue
                if contest['freeze'] > 0:
                    if submission['created_at'] > contest['start'] + timedelta(minutes=contest['freeze']):
                        continue
            if submission['verdict_id'] == VERDICT_AC:
                users[user_id]['problems'][problem_id]['ac_time'] = (submission['created_at'] - contest['start']).seconds // 60
                problems[problem_id]['ac'] += 1
            users[user_id]['problems'][problem_id]['verdict_id'] = submission['verdict_id']
        # iterate user list to update user info
        users = list(users[x] for x in users)
        for user in users:
            # remove personal info
            user['attempt'] = 0
            user['penalty'] = 0
            user['ac'] = 0
            user['problems'] = list(user['problems'][x] for x in user['problems'])
            for problem in user['problems']:
                if problem['ac_time']:
                    problem['penalty'] = problem['ac_time']
                    problem['penalty'] += (problem['attempt'] - 1) * PENALTY
                else:
                    problem['penalty'] = 0
                user['attempt'] += problem['attempt']
                user['penalty'] += problem['penalty']
                user['ac'] += problem['verdict_id'] == VERDICT_AC
        problems = list(problems[x] for x in problems)
        # sort
        users = sorted(users, key = lambda x: (-x['ac'], x['penalty']))
        now_rank = 0
        now_rank_idx = (1, 0)
        for user in users:
            if now_rank_idx != (-user['ac'], user['penalty']):
                now_rank += 1
                now_rank_idx = (-user['ac'], user['penalty'])
            user['rank'] = now_rank
        res = {}
        res['users'] = users
        res['problems'] = problems
        yield self.db.execute('UPDATE scoreboard SET data = %s WHERE id = %s;', (json.dumps(res, cls=DatetimeEncoder), data['type'],))
        return (None, res)
