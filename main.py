import os
import platform
import sys
import time
from datetime import datetime
from pprint import pprint
import subprocess
import psutil
import cpuinfo

start_time = time.time()


# func 1
def general_info():
    result = {}
    inf = platform.uname()
    result['win'] = inf.system + inf.release + ' ' + inf.version + ' ' + inf.machine
    result['name'] = inf.node
    result['proc'] = process_inf()['name']
    return result


# func 3
def process_inf(need_all=True):
    result = {}
    if need_all:
        processor_name = cpuinfo.get_cpu_info()['brand_raw']
        result['name'] = processor_name
        architecture = platform.architecture()[0]
        result['arch'] = architecture
    cores = psutil.cpu_count()
    result['log_cores'] = cores
    result['freq'] = psutil.cpu_freq().current
    cores = []
    for percentage in psutil.cpu_percent(percpu=True, interval=1):
        cores.append(percentage)
    result['cores'] = cores
    result['usage'] = psutil.cpu_percent()
    return result


# func 2
def time_on():
    boottime = psutil.boot_time()
    bt = datetime.fromtimestamp(boottime)
    return f"When pc on: {bt.hour}:{bt.minute}:{bt.second} {bt.day}/{bt.month}/{bt.year}"


# extra func
def translate(n, s='B'):
    factor = 1024
    for i in ["", "K", "M", "G", "T", "P"]:
        if n < factor:
            return f"{n:.2f}{i}{s}"
        n /= factor


# func 5
def disk():
    result = {}
    for i in psutil.disk_partitions():
        now = {}
        n = psutil.disk_usage(i.device)
        now['total'] = translate(n.total)
        now['used'] = translate(n.used)
        now['free'] = translate(n.free)
        now['procent'] = n.percent, '%'
        result[i.device] = now
    return result


# pprint(general_info())
print("--- %s seconds ---" % round(time.time() - start_time, 5))
pprint(disk())
