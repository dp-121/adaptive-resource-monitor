import psutil
import os
import subprocess
from collections import deque
import time

cpu_history = deque(maxlen=30)
memory_history = deque(maxlen=30)

def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()

    cpu_history.append(cpu_percent)
    memory_history.append(memory.percent)

    top_processes = sorted(
        psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']),
        key=lambda p: p.info['cpu_percent'],
        reverse=True
    )[:5]

    processes_info = []
    for p in top_processes:
        try:
            processes_info.append({
                "pid": p.info['pid'],
                "name": p.info['name'],
                "cpu": p.info['cpu_percent'],
                "memory": round(p.info['memory_info'].rss / (1024 * 1024), 2)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return {
        "cpu": cpu_percent,
        "memory_percent": memory.percent,
        "cpu_history": list(cpu_history),
        "memory_history": list(memory_history),
        "top_processes": processes_info
    }

def simulate_cpu_load():
    os.system("python3 -c 'while True: pass' &")

def simulate_memory_load():
    os.system("python3 -c 'a = [0]*10**7; import time; time.sleep(60)' &")

def reset_simulation():
    subprocess.call("pkill -f 'python3 -c'", shell=True)

def adaptive_reallocate(threshold=80):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            cpu = proc.cpu_percent(interval=0.1)
            if cpu > threshold:
                proc.nice(10)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        for _ in range(3):
            proc.kill()
            time.sleep(0.5)
            if not proc.is_running():
                return True
        return False
    except Exception:
        return False
