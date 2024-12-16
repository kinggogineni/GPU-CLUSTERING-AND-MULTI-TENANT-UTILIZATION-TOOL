import psutil
import time

def allocate_cpu_cores():
    available_cores = psutil.cpu_count(logical=False)
    print(f"Total available cores: {available_cores}")

    while True:
        # Check current CPU utilization
        cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        print(f"CPU Usage per Core: {cpu_usage}")

        # Dynamic Allocation Logic
        for i, usage in enumerate(cpu_usage):
            if usage < 50:
                print(f"Core {i} is under-utilized; can allocate more tasks.")
            else:
                print(f"Core {i} is fully utilized; consider deallocating tasks.")

        time.sleep(2)  # Adjust to control the allocation frequency

if __name__ == "__main__":
    allocate_cpu_cores()

