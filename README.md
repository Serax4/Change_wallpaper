# Change_wallpaper
Following these simple steps you will be able to have a new background wallpaper (from a selected bunch) at startup on Windows 10/11.

Implementation Steps

Step 1: Prepare Your Directory
  Create a directory and fill it with your desired images
Step 2: Install Python
Step 3: Download the script
Step 4: Run the Script
  Open a terminal or command prompt.
  Run the script using:
    python path\to\script.py
  Replace path\to with the full path where the script is located.
Step 5: Automate with Task Scheduler
  Open Task Scheduler in Windows.
    Create a new task.
      Set the trigger to run "At log on" or "Daily."
    Set the action to run the Python script:
      Action: Start a Program
      Program/script: path/pythonw (You can find the path using 'where pythonw' in cmd)
      Add arguments:  path\to\script.py (Be careful to add a space before the arguments)
  
  Using pythonw instead of python in the Task Scheduler will avoid showing a terminal window.
