import os
import subprocess

print("📰 Daily news check initiated...")

# 1. Grab your desktop visual security keys
os.environ["DISPLAY"] = ":0"
os.environ["XAUTHORITY"] = "/home/mamoona/.Xauthority"

# 2. Tell Chrome exactly which Linux user runtime directory to use
# This prevents Chrome from freezing when called by background tasks like cron!
os.environ["XDG_RUNTIME_DIR"] = "/run/user/1000"

# Run native Ubuntu pop-up layout window
popup_command = (
    'zenity --question '
    '--title="Daily News Prompt" '
    '--text="Your scheduled time has arrived! Do you want to open the live news feed right now?" '
    '--width=350'
)

exit_status = os.system(popup_command)

# Zenity returns an exit status of 0 if the user clicks 'Yes'
if exit_status == 0:
    print("User clicked YES. Launching Google Chrome directly via system environment...")
    
    # Using a clean subprocess command to launch your system browser cleanly under cron
    # 'gio open' forces Ubuntu to handle the link launch using your default browser
    subprocess.Popen(['gio', 'open', 'https://bbc.com'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
else:
    print("User clicked NO or closed the prompt window. Exiting safely...")

