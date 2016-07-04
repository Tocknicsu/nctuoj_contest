from req import Service
from service.base import BaseService
import datetime
import time
import psutil

class System(BaseService):
    net_tx, net_rx, net_last_time = psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv, time.time()
    def get_time(self):
        return (None, datetime.datetime.now())

    def get_cpu(self):
        cpus = psutil.cpu_percent(percpu=True)
        return (None, sum(cpus) / len(cpus))

    def get_memory(self):
        return (None, psutil.virtual_memory().percent)

    def get_network(self):
        net_io = psutil.net_io_counters()
        now = time.time()
        tx = (net_io.bytes_sent - System.net_tx) / (now - System.net_last_time)
        rx = (net_io.bytes_recv - System.net_rx) / (now - System.net_last_time)
        System.net_tx, System.net_rx, System.net_last_time = net_io.bytes_sent, net_io.bytes_recv, now
        return (None, {'tx': tx, 'rx': rx})

    def get_all(self):
        res = {}
        res['time'] = self.get_time()[1]
        res['cpu'] = self.get_cpu()[1]
        res['memory'] = self.get_memory()[1]
        res['network'] = self.get_network()[1]
        return (None, res)
