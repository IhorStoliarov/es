import psutil
while True:
    cpu_proc = psutil.cpu_percent(interval=1)
    cpu_stat = psutil.cpu_stats()
    cpu_freq = psutil.cpu_freq()
    mem = psutil.virtual_memory()
    mem_us = psutil.virtual_memory()
    mem_active = psutil.virtual_memory()
    print(cpu_proc)
    print(cpu_stat)
    print(cpu_freq)
    print(mem)
    print(mem_us)
    print(mem_active)
    print(psutil.net_connections(kind="inet4"))
    print(psutil.net_if_addrs())
    print(psutil.net_if_stats())
    print(psutil.users())
    print(psutil.Process().exe())

