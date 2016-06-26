from req import Service
from service.base import BaseService


class Execute(BaseService):
    def get_execute_list(self):
        res = yield self.db.execute("SELECT id, description FROM execute_types ORDER BY id ASC")
        res = res.fetchall()
        return (None, res)

    def get_execute(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = (yield self.db.execute("SELECT * FROM execute_types WHERE id=%s", (data['id'],))).fetchone()
        return (None, res)

    def get_execute_with_steps(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = (yield self.db.execute("SELECT * FROM execute_types WHERE id=%s", (data['id'],))).fetchone()
        res['commands'] = (yield self.db.execute("SELECT es.command FROM execute_types as e, execute_steps as es WHERE e.id=es.execute_type_id AND e.id=%s ORDER BY es.id", (data['id'],))).fetchall()
        return (None, res)

    def post_execute(self, data={}):
        required_args = [{
            'name': '+commands',
            'type': list,
        }, {
            'name': '+description',
            'type': str,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        res = yield self.db.execute("INSERT INTO execute_types (description) VALUES (%s) RETURNING id", (data['description'],))
        res = res.fetchone()
        for x in data['commands']:
            yield self.db.execute("INSERT INTO execute_steps (execute_type_id, command) VALUES (%s, %s)", (res['id'], x,))
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
            yield self.db.execute("INSERT INTO execute_steps (execute_type_id, command) VALUES (%s, %s)", (data['id'], x,))
        return (None, None)

    def delete_execute(self, data={}):
        required_args = [{
            'name': '+id',
            'type': int,
        }]
        err = self.form_validation(data, required_args)
        if err: return (err, None)
        yield self.db.execute("DELETE FROM execute_types WHERE id=%s", (data['id'],))
        return (None, None)
