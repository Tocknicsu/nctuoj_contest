from req import Service
from service.base import BaseService


class Execute(BaseService):
    def get_execute_list(self):
        res = yield self.db.execute("SELECT id, description, priority FROM execute_types ORDER BY priority ASC")
        res = res.fetchall()
        return (None, res)

    def get_execute(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("SELECT es.command FROM execute_types as e, execute_steps as es WHERE e.id=es.execute_type_id AND e.id=%s ORDER BY es.id", (data['id'],))
        res = res.fetchall()
        return (None, res)

    def put_execute(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }, {
            'name': '+commands',
            'type': list,
        }, {
            'name': '+description',
            'type': str,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("DELETE FROM execute_steps WHERE execute_type_id=%s", (data['id'],))
        for x in data['commands']:
            res = yield self.db.execute("INSERT INTO execute_steps (execute_type_id, command) VALUES (%s, %s)", (data['id'], x,))
        return (None, None)

