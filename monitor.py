# --- IMPORTS ---
# Import the psutil library, which is a cross-platform library for retrieving
# information on running processes and system utilization (CPU, memory, disks, network, sensors).
import psutil
# Import the time library to be able to pause the script execution.
import time
# Import the datetime object from the datetime library to get timestamps for our logs.
from datetime import datetime

# --- AUTHOR ---
# Author: Daniel Chisasura

# --- CONFIGURATION ---
# Define the CPU usage percentage that will trigger an alert.
CPU_THRESHOLD = 80.0  # Alert if CPU usage is over 80%
# Define the number of seconds the script should wait between each check.
MONITOR_INTERVAL = 5 # Check every 5 seconds

# --- MAIN MONITORING FUNCTION ---
def monitor_system():
    """
    This function contains an infinite loop that continuously monitors the system's CPU usage.
    If the usage exceeds the defined threshold, it prints a formatted alert message to the console.
    The loop can be stopped gracefully by the user by pressing Ctrl+C.
    """
    # --- SCRIPT STARTUP ---
    print("📈 Starting System Monitor...")
    print(f"Alert threshold set to {CPU_THRESHOLD}% CPU usage.")
    print(f"Checking every {MONITOR_INTERVAL} seconds.")
    print("Press Ctrl+C to stop.")
    
    # --- ERROR HANDLING AND MAIN LOOP ---
    try:
        # 'while True' creates a loop that will run forever unless it's explicitly broken
        # or an exception occurs (like the user pressing Ctrl+C).
        while True:
            # --- DATA COLLECTION ---
            # Call psutil.cpu_percent() to get the system-wide CPU utilization as a percentage.
            # The 'interval=1' argument means it will compare CPU times over a 1-second interval,
            # which provides a more accurate, non-instantaneous reading.
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Get the current system time.
            now = datetime.now()
            # Format the time into a human-readable string (e.g., "2025-08-26 12:30:00").
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            
            # --- LOGGING AND ALERTING ---
            # Print the current status. The '\r' at the end moves the cursor to the
            # beginning of the line, and 'end=""' prevents a newline, creating a
            # single, updating line of text. (Note: this is a more advanced option, a simple print is also fine)
            print(f"[{current_time}] Current CPU Usage: {cpu_usage}%  ")
            
            # Check if the measured CPU usage is greater than our defined threshold.
            if cpu_usage > CPU_THRESHOLD:
                # If it is, print a multi-line alert message to make it stand out.
                print(f"🚨 ALERT! 🚨")
                print(f"[{current_time}] High CPU usage detected: {cpu_usage}%")
                print(f"This is above the threshold of {CPU_THRESHOLD}%.")
                print("-------------------------------------------------")

            # --- PAUSE EXECUTION ---
            # Use time.sleep() to pause the script for the number of seconds
            # defined in MONITOR_INTERVAL. This prevents the script from consuming
            # too much CPU itself by running in a tight, constant loop.
            time.sleep(MONITOR_INTERVAL)

    # The 'except' block catches specific errors.
    except KeyboardInterrupt:
        # A KeyboardInterrupt exception is raised when the user presses Ctrl+C.
        # This allows us to "catch" the exit signal and print a clean shutdown message
        # instead of a messy error traceback.
        print("\n👋 Monitor stopped by user. Exiting.")
    except Exception as e:
        # This is a general catch-all for any other unexpected errors that might occur.
        print(f"\n🚫 An unexpected error occurred: {e}")

# --- SCRIPT EXECUTION ---
if __name__ == "__main__":
    # Call the main monitoring function to start the loop.
    monitor_system()