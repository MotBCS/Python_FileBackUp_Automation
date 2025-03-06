# Simple Automatic Folder Backup - Python

# Imports
# -----------------
# Operating System
import os
# For Copying Operations
import shutil
# Save Date of Backed Up Folder
import datetime
import schedule
import time

# -------------------
# Source Directory
source_dir = "/Users/mya/Desktop/TIP101S4"

# Destination Directory
destination_dir = "/Users/mya/Desktop/TIP101_BackUp"


# Function takes in two parameters 'source' and 'destination'
def copy_to_directory(source, destination):
    # Returns the current date
    today = datetime.date.today()

    # Takes the passed in destination directory and combines with a string of today's date
    dest_dir = os.path.join(destination, str(today))

    try:
        # Copy everything in the folder recursively, copy from source to destination directory
        shutil.copytree(source, dest_dir)
        print(f"Folder Copied To: {dest_dir}")
    except FileExistsError:
        print(f"Folder Already Exist In: {destination}")


# Schedule To Run At A Certain Specified Time
# .do calls the lambda function and completes the wrapped function and passes in parameters
schedule.every().monday.at("18:30").do(lambda: copy_to_directory(source_dir, destination_dir))

while True:
    # Consistently run the scheduled task that have not run
    schedule.run_pending()
    # Sleeps for 60 seconds before running next task
    time.sleep(60)

# copy_to_directory(source_dir, destination_dir)

# Installed Modules
# pip install schedule // Schedules a task to run
