# Simple Automatic Folder Backup - Python

A short python script to automate the process of backing up folders to specific destination on a scheduled basis. It copies the content of a source directory into a nre folder within the destination directory labeles with the current date.

- Automatically copies a folder to the backup location
- Runs on set schedule (Every Monday at 6:30PM - To backup class preperation files)
- Prevents duplicated backups by checking if the backup already exists
- Simple and lightweight, using Python's built in libraries

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/0342fbb37d1446b78fd3d19014171f26?sid=739c4d45-4c45-4abc-bee1-a57daa8e41d8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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

