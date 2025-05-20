# taskbar_worker.py

import win32gui
import win32con
import win32api
import win32process
import win32com.client
import ctypes
import time
import logging
import os

# Logging setup
log_path = os.path.join(os.getenv("TEMP"), "taskbar_worker.log")
logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(message)s")

def get_taskbar_hwnd():
    return win32gui.FindWindow("Shell_TrayWnd", None)

def is_cursor_over_taskbar(taskbar_rect):
    x, y = win32api.GetCursorPos()
    left, top, right, bottom = taskbar_rect
    return left <= x <= right and top <= y <= bottom

def is_windows_key_pressed():
    VK_LWIN = 0x5B
    VK_RWIN = 0x5C
    return win32api.GetAsyncKeyState(VK_LWIN) < 0 or win32api.GetAsyncKeyState(VK_RWIN) < 0

def is_desktop_focused():
    try:
        hwnd = win32gui.GetForegroundWindow()
        shell = win32com.client.Dispatch("Shell.Application")
        desktop_hwnd = shell.Windows().Item().HWND
        return hwnd == desktop_hwnd or win32gui.GetClassName(hwnd) in ["Progman", "WorkerW"]
    except Exception as e:
        logging.warning(f"Focus check error: {e}")
        return False

def hide_taskbar(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    logging.info("Taskbar hidden")

def show_taskbar(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    logging.info("Taskbar shown")

def main():
    hwnd = get_taskbar_hwnd()
    if not hwnd:
        logging.error("Taskbar not found.")
        return
    logging.info(f"✅ Taskbar found: HWND = {hwnd}")

    last_visible = True

    try:
        while True:
            try:
                rect = win32gui.GetWindowRect(hwnd)
                over_taskbar = is_cursor_over_taskbar(rect)
                win_key = is_windows_key_pressed()
                on_desktop = is_desktop_focused()

                should_show = over_taskbar or win_key or not on_desktop

                if should_show and not last_visible:
                    show_taskbar(hwnd)
                    last_visible = True
                elif not should_show and last_visible:
                    hide_taskbar(hwnd)
                    last_visible = False

                time.sleep(0.01)  # very responsive
            except Exception as e:
                logging.exception("Recoverable error in loop")
                continue
    except Exception as e:
        logging.exception("Fatal error in outer loop")
    finally:
        show_taskbar(hwnd)
        logging.info("Taskbar shown on exit")


if __name__ == "__main__":
    main()
