import inspect
import re

def get_module_path(obj):
    path = inspect.getmodule(obj)
    path = re.match("<module '(.*)' from .*", str(path)).groups()[0]
    return (path, obj.__class__.__name__)
