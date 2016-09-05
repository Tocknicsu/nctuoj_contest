import logging
import inspect

def log(msg):
    (frame, filename, line_number, function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
    print("[%s,%s,%s] %s"%(filename, line_number, function_name, msg))

