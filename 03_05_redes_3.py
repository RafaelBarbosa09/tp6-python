import psutil
import time

for i in range(5):
    print(psutil.net_io_counters())
    time.sleep(1)
