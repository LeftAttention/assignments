import psutil
import time
import sys

def monitor_cpu(threshold=80):
    """
    Continuously monitor CPU usage and raise an alert if it exceeds the threshold.
    
    Parameters:
        threshold (int): The CPU usage threshold for triggering an alert. Default is 80.
    """
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            print(f"Current CPU usage: {cpu_percent}%")
            
            if cpu_percent > threshold:
                print(f"ALERT: CPU usage exceeded {threshold}%")
                
            time.sleep(1)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting to monitor CPU usage...")
    monitor_cpu()
