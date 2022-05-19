import psutil
import time

p = psutil.Process()
time = p.create_time()
print(p)
print(time)
print(p.status())
print(p.name())
