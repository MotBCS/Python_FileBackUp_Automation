# Simple Automatic Folder Backup - Python

A short python script to automate the process of backing up folders to specific destination on a scheduled basis. It copies the content of a source directory into a nre folder within the destination directory labeles with the current date.

- Automatically copies a folder to the backup location
- Runs on set schedule (Every Monday at 6:30PM - To backup class preperation files)
- Prevents duplicated backups by checking if the backup already exists
- Simple and lightweight, using Python's built in libraries

# Requirements
- Python 3.x
- 'schedule' module (install with pip install schedule)

# Installation & Setup
- Git clone this repository
- Cd into folder
- Install dependencies (pip install schedule)
- Update source directory and destination directory
- Modify the schedule to your needs

- Run Script (python backup_automationpy)

