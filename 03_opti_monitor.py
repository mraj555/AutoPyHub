import os          # Provides OS-dependent functions like clearing the terminal
import psutil      # Third-party library to fetch system and hardware info
import time        # Used to pause execution between updates

def clear_screen():
    """
    Clear the terminal screen.
    Uses 'cls' on Windows ('nt') and 'clear' on Unix-like systems.
    """
    os.system("cls" if os.name == "nt" else "clear")

def show_stats():
    """
    Fetch and display current CPU, RAM, and disk usage.
    All values are shown as percentages and in GB where applicable.
    """
    print("🖥️ System Monitoring Software 🖥️")

    # CPU usage: measures over 1-second interval for accuracy
    cpu = psutil.cpu_percent(interval=1)

    # RAM usage: get total, used, and percentage
    ram = psutil.virtual_memory()

    # Disk usage: get total, used, and percentage for root partition
    disk = psutil.disk_usage("/")

    # Display CPU load
    print(f"CPU Usage = {cpu}%")

    # Display RAM load with used/total in GB
    print(
        f"RAM Usage = {ram.percent}% "
        f"({round(ram.used / 1024**3, 2)}GB/"
        f"{round(ram.total / 1024**3, 2)}GB)"
    )

    # Display disk load with used/total in GB
    print(
        f"Disk Usage = {disk.percent}% "
        f"({round(disk.used / 1024**3, 2)}GB/"
        f"{round(disk.total / 1024**3, 2)}GB)"
    )

    # Separator line for readability
    print("=" * 40)

if __name__ == "__main__":
    # Main loop: refresh stats every 3 seconds until user presses Ctrl+C
    try:
        while True:
            clear_screen()   # Clear old data from screen
            show_stats()     # Print updated stats
            time.sleep(3)    # Wait 3 seconds before next update
    except KeyboardInterrupt:
        # Graceful exit message when user stops the program
        print("❌ Monitoring stopped.")
