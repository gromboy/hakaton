import platform
import time
from datetime import datetime
from pprint import pprint

import psutil
import cpuinfo

start_time = time.time()


def process_inf(need_all=True):
    result = {}
    if need_all:
        processor_name = cpuinfo.get_cpu_info()['brand_raw']
        result['name'] = processor_name
        architecture = platform.architecture()[0]
        result['arch'] = architecture
    cores = psutil.cpu_count()
    result['log_cores'] = cores
    result['freq'] = psutil.cpu_freq().currentcp
    cores = []
    for percentage in psutil.cpu_percent(percpu=True, interval=1):
        cores.append(percentage)
    result['cores'] = cores
    result['usage'] = psutil.cpu_percent()
    return result


def time_on():
    boottime = psutil.boot_time()
    bt = datetime.fromtimestamp(boottime)
    print(f"When pc on: {bt.hour}:{bt.minute}:{bt.second} {bt.day}/{bt.month}/{bt.year}")

pprint(process_inf(False))
print("--- %s seconds ---" % round(time.time() - start_time, 3))
