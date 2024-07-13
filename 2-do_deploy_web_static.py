#!/usr/bin/python3
"""
Fabric script to deploy an archive to web servers
"""
from fabric.api import env, put, run, local
from datetime import datetime
import os


# Define remote servers
env.hosts = ['54.165.77.76', '34.239.248.129']
env.user = 'ubuntu'
env.key_filename = ['~/.ssh/school']

def do_deploy(archive_path):
    """Deploys archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ on the web server
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/<archive filename without extension>/
        archive_filename = os.path.basename(archive_path)
        archive_name = os.path.splitext(archive_filename)[0]
        release_path = f'/data/web_static/releases/{archive_name}/'
        run(f'mkdir -p {release_path}')
        run(f'tar -xzf /tmp/{archive_filename} -C {release_path}')

        # Delete archive from server
        run(f'rm /tmp/{archive_filename}')

        # Move contents out of nested web_static directory if necessary
        run(f'mv {release_path}web_static/* {release_path}')
        run(f'rm -rf {release_path}web_static')

        # Remove existing symbolic link
        current_link = '/data/web_static/current'
        run(f'rm -rf {current_link}')

        # Create new symbolic link
        run(f'ln -s {release_path} {current_link}')

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
