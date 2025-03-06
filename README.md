# Simple Automatic Folder Backup - Python

This is a short Python script to automate the process of backing up folders to a specific destination on a scheduled basis. It copies the content of a source directory into a new folder within the destination directory labeled with the current date.

- Automatically copies a folder to the backup location
- Runs on a set schedule (Every Monday at 6:30 PM - To backup class preparation files)
- Prevents duplicated backups by checking if the backup already exists
- Simple and lightweight, using Python's built-in libraries

<div style="position: relative; padding-bottom: 56.25%; height: 0;"><iframe src="https://www.loom.com/embed/0342fbb37d1446b78fd3d19014171f26?sid=66393d8a-9055-45e7-86ae-66f9e27ac5ca" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


# Requirements
- Python 3.x
- 'schedule' module (install with pip install schedule)

# Installation & Setup
- Git clone this repository
- Cd into folder
- Install dependencies (pip install schedule)
- Update the source directory and destination directory
- Modify the schedule to your needs

- Run Script (python backup_automationpy)

