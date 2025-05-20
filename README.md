Taskbar Hider Utility
=====================

Overview:
---------
This utility consists of two Python scripts:
1. taskbar_worker.pyw - A background process that dynamically hides/shows the Windows taskbar.
2. taskbar_manager.py - A simple terminal UI to launch the taskbar hider silently, optional.

The worker hides the taskbar when the desktop is focused and the mouse isn't hovering over it.
It shows the taskbar again if:
- The mouse is near the taskbar
- The Windows key is pressed
- The desktop is not focused(an app is running on it, with the mouse clicked on it. If you click the mouse on the screen, the TB will dissapear.)

Requirements:
-------------
- Windows OS
- Python 3.x
- pywin32 package

To install dependencies:
------------------------
Open Command Prompt and run:

    pip install pywin32

or 

	pip install -r requirements.txt

How to Use:
-----------
1. Run taskbar_manager.py from a terminal:

    python taskbar_manager.py

2. Choose option [1] to launch the taskbar hider silently.

3. To stop it, you can:
    - Manually kill the pythonw process from Task Manager
    - Restart your computer (if running persistently)
    - Modify the script to add a stop function if needed

Startup Option (Optional):
--------------------------
If you want the taskbar hider to launch automatically on startup:

- Create a task in TASK SCHEDULER, and put taskbar_worker.pyw in the task.
- If you dont know how to create a task, here's a video: 
https://www.youtube.com/watch?v=T9A8TelGsdo&ab_channel=Jean-ChristopheChouinard
(credits to Jean-Christophe Chouinard for the video)

Logging:
--------
Logs are saved in your TEMP folder:
- taskbar_worker.log
- taskbar_manager.log

These logs track start, stop, and error messages for debugging.

---

** Made by execRooted **
