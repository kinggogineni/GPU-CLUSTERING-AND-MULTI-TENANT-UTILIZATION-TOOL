# gpu_clustering.py
import psutil
import numpy as np

def get_system_info():
    # Get CPU information
    cpu_count = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq().max
    memory_info = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB

    # Simulate GPU information
    gpu_info = {
        "gpu_count": cpu_count // 2,  # Simulate half of CPU cores as GPUs
        "gpu_memory": memory_info / 2,  # Simulate half of system memory as GPU memory
        "gpu_frequency": cpu_freq / 2  # Simulate GPU frequency as half of CPU frequency
    }

    return {
        "cpu_count": cpu_count,
        "cpu_frequency": cpu_freq,
        "memory": memory_info,
        "gpu_info": gpu_info
    }

if __name__ == "__main__":
    system_info = get_system_info()
    print(system_info)
