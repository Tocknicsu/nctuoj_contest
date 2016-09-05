from req import Service
from service.base import BaseService


class DB(BaseService):
    def delete_table(self, data={}):
        required_args = [{
            'name': '+name',
            'type': str,
        }]
        err = self.form_validation(data,required_args)
        if err:
            return (err, None)
        yield self.db.execute('TRUNCATE %s RESTART IDENTITY CASCADE', (data['name'],))
        return (None, None)

