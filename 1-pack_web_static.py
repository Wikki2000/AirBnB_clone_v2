#!/usr/bin/python3
"""Compress web static package
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to compress directory

    Return: path to archive on success; None on fail
    """
    # Get current time and create archive path
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = f'versions/web_static_{now}.tgz'

    # Create archive
    local('mkdir -p versions/')
    result = local(f'tar -cvzf {archive_path} web_static/')

    # Check if archiving was successful
    if result.succeeded:
        return archive_path
    return None
