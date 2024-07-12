#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to compress directory

    Return: path to archive on success; None on fail
    """
    # Get current time
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    # Create archive
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    # Check if archiving was successful
    if result.succeeded:
        return archive_path
    return None
"""
Uncomment out if u want to run with python3 <file_name>
archive_path = do_pack()
if archive_path:
    print(f"Archive created at: {archive_path}")
else:
    print("Failed to create archive")
"""
