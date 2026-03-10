#!/usr/bin/env python3
import os
import datetime

now = datetime.datetime.now()
# Example: delete old files from a folder
folder = "/tmp/test_cleanup"

print(f"Cleanup started at {now}")

# just an example, won't delete anything critical
if os.path.exists(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder,filename)
        if os.path.isfile(filepath):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

print(f"Cleanup finished at {datetime.datetime.now()}")
