import os
import subprocess

print("📰 Daily news check initiated...")

# Grab ur desktop visual security keys
os.environ["DISPLAY"] = ":0"
os.environ["XAUTHORITY"] = "/home/mamoona/.Xauthority"

# Tell Chrome exactly which Linux user runtime directory to use
# This prevents Chrome from freezing when called by background tasks like cron!
os.environ["XDG_RUNTIME_DIR"] = "/run/user/1000"


popup_command = (
    'zenity --question '
    '--title="Daily News Prompt" '
    '--text="Your scheduled time has arrived! Do you want to open the live news feed right now?" '
    '--width=350'
)

exit_status = os.system(popup_command)


if exit_status == 0:
    print("User clicked YES. Launching Google Chrome directly via system environment...")
    
    
    # 'gio open' forces Ubuntu to handle the link launch using your default browser
    subprocess.Popen(['gio', 'open', 'https://bbc.com'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
else:
    print("User clicked NO or closed the prompt window. Exiting safely...")

