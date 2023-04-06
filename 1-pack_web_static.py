#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a compressed archive of the web_static folder.
    The archive will be saved in the versions folder.
    """
    local('mkdir -p versions')

    time_format = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time_format)

    try:
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None
