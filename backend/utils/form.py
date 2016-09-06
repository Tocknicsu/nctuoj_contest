from dateutil import parser
from datetime import datetime
def form_validation(form ,schema):
    err = _form_validation(form, schema)
    return (400, err) if err else None
def _form_validation(form, schema):
    '''
    schema:
        [{
            ### require
            'name': <str> # +<str> means require, default is optional
            ### optional
            'type': <class>
            'non_empty': <bool> # for str, list
            'except': <list>
            'range': <tuple> # t[0] <= value <= t[1]
            'len_range': <tuple> # t[0] <= len(value) <= t[1]
            'check_dict': <dict> # for dict
            'xss': <bool> # xss filter, default is False
            ...
        }]
    int
    str
    list
    set
    dict
    datetime
    '''
    key = list(form.keys())
    for item in key:
        exist = False
        for x in schema:
            if x['name'] == item or (x['name'][0] == '+' and x['name'][1:] == item):
                exist = True
        if not exist:
            del form[item]


    for item in schema:
        require = True if item['name'][0] == '+' else False
        name = item['name'] = item['name'][1:] if require else item['name']

        ### check require
        if require and (name not in form or form[name] is None):
            return '%s not in form' % name

        
        if not require and (name not in form or form[name] is None):
            form[name] = None
            continue

        ## check non_empty
        if 'non_empty' in item and item['non_empty']:
            if form[name] == item['type']() or form[name] is None:
                return 'value of %s: "%s" should not be empty value' % (name, str(form[name]))

        ### check value type
        if 'type' in item:
            if not isinstance(form[name], item['type']):
                if item['type'] == datetime:
                    try: form[name] = parser.parse(form[name])
                    except Exception as e: return name + str(e)
                else:
                    try: form[name] = item['type'](form[name])
                    except Exception as e: return name + str(e)


        ### check except
        if 'except' in item:
            if form[name] in item['except']:
                return 'value of %s: "%s" in except list' % (name, str(form[name]))
        
        ### check range
        if 'range' in item:
            if not (item['range'][0] <= form[name] <= item['range'][1]):
                return 'value of %s: "%s" not in range %s' % (name, str(form[name]), str(item['range']))

        ### check len_range
        if 'len_range' in item:
            if not (item['len_range'][0] <= len(form[name]) <= item['len_range'][1]):
                return 'value of %s: "%s" not in len_range %s' % (name, str(form[name]), str(item['len_range']))

        ### check check_dict
        if 'check_dict' in item:
            err = form_validation(form[name], item['check_dict'])
            if err: return err

    return None
