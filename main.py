import platform
import time
from datetime import datetime
from pprint import pprint
import psutil
import cpuinfo
import wmi

start_time = time.time()


# func 1
def general_info():
    result = {}
    inf = platform.uname()
    result['Версия OC'] = inf.system + inf.release + ' ' + inf.version + ' ' + inf.machine
    result['Имя компьютера'] = inf.node
    result['Процессор'] = process_inf()['Название']
    result['Видеокарта'] = [i.Name for i in wmi.WMI().Win32_VideoController()]
    c = wmi.WMI()
    for bios_id in c.Win32_BIOS():
        result["BIOS"] = bios_id.SerialNumber.strip()
    return result


# func 3
def process_inf(need_all=True):
    result = {}
    if need_all:
        processor_name = cpuinfo.get_cpu_info()['brand_raw']
        result['Название'] = processor_name
        architecture = platform.architecture()[0]
        result['Архитектура'] = architecture
    cores = psutil.cpu_count()
    result['Логических процессоров'] = cores
    result['Тактовая частота'] = str(psutil.cpu_freq().current) + ' Ггц'
    cores = []
    for percentage in psutil.cpu_percent(percpu=True, interval=1):
        cores.append(percentage)
    result['Ядра'] = cores
    result['Использование'] = psutil.cpu_percent()
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


def op():
    result = {}
    n = psutil.virtual_memory()
    result['vsego'] = translate(n.total)
    result['dostupnaya'] = translate(n.available)
    result['procent zanyato'] = str(n.percent) + '%'
    result['ispolzuetsya'] = translate(n.used)
    return result


if __name__ == '__main__':
    pprint(process_inf())
    print("--- %s seconds ---" % round(time.time() - start_time, 5))

# pip install -r requirements.txt
