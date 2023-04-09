#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""

from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['100.26.178.47 web-01', '100.26.214.157 web-02']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_deploy(archive_path):
    """Deploys the web static to the web servers"""
    if not exists(archive_path):
        return False

    # Create directories
    try:
        put(archive_path, "/tmp/")
        archive_file = archive_path.split("/")[-1]
        archive_dir = "/data/web_static/releases/" + \
                      archive_file.split(".")[0]
        run("sudo mkdir -p {}".format(archive_dir))

        # Uncompress archive
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_file,
                                                 archive_dir))

        # Delete archive
        run("sudo rm /tmp/{}".format(archive_file))

        # Move files out of archive dir
        run("sudo mv {}/web_static/* {}/".format(archive_dir, archive_dir))

        # Remove empty archive dir
        run("sudo rm -rf {}/web_static".format(archive_dir))

        # Delete current symlink
        run("sudo rm -rf /data/web_static/current")

        # Create new symlink
        run("sudo ln -s {} /data/web_static/current".format(archive_dir))
        return True
    except:
        return False

