import os
import sys
import shutil
import subprocess
import logging
import win32gui
import win32con
import time

# ANSI color codes (use only if terminal supports it)
BLUE = "\033[94m" if sys.stdout.isatty() else ""
RESET = "\033[0m" if sys.stdout.isatty() else ""

# Logging setup
log_path = os.path.join(os.getenv("TEMP"), "taskbar_manager.log")
logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(message)s")

# Paths
STARTUP_DIR = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
WORKER_FILENAME = "taskbar_worker.pyw"
WORKER_PATH = os.path.join(SCRIPT_DIR, WORKER_FILENAME)
STARTUP_PATH = os.path.join(STARTUP_DIR, WORKER_FILENAME)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()

def typewriter(text):
    delay = 0.04  # Typing effect
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def run_worker():
    try:
        subprocess.Popen(['pythonw', WORKER_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        typewriter("[+] Launched taskbar worker silently.")
        logging.info("Worker launched via pythonw.")
    except Exception as e:
        typewriter(f"[-] Failed to launch worker: {e}")
        logging.exception("Worker launch failed.")

def logo():
    print(f"""{BLUE}
   \\     /  
    \\   /   
     \\ /    
      |     
      |     
      |     
      |     
   _________
  |   TBH   |
  |_________|
{RESET}""")

def help()

    


def main_menu():
    while True:
        clear()
        typewriter("=== Taskbar Hider Manager ===")
        typewriter("1. Launch taskbar hiding")
        typewriter("2. Help")
        typewriter("3. Exit")
        choice = input("Select an option: ").strip()

        clear()

        if choice == "1":
            run_worker()
        elif choice == "2":
            typewriter("Exiting...")
            break
        elif choice == 2
            help()
        else:
            typewriter("[-] Choice not available. Choose 1 or 2.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
