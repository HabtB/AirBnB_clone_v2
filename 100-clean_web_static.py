#!/usr/bin/env python3

import os
from fabric.api import env, local, put, run
from fabric.context_managers import cd
from fabric.contrib.files import exists
from datetime import datetime


env.hosts = ['100.26.178.47', '100.26.214.157']
env.user = 'ubuntu'


def do_pack():
    """
    Compress the contents of the web_static directory into a tgz archive.

    Returns:
        The path to the compressed archive on the local machine.
    """
    local('mkdir -p versions')
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(timestamp)
    local('tar -czf {} web_static'.format(archive_path))
    size = os.path.getsize(archive_path)
    print('web_static packed: {} -> {}Bytes'.format(archive_path,:
        return False

    if run('rm {}'.format(remote_path)).failed:
        return False

    with cd(dirname):
        run('mv web_static/* .')
        run('rm -rf web_static')

    with cd('/data/web_static'):
        if exists('current'):
           size))
    return archive_path


def do_deploy(archive_path):
    """
    Deploy the contents of the compressed archive to the web server.

    Args:
        archive_path: The path to the compressed archive on the local machine.

    Returns:
        True if the deployment was successful, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    remote_path = '/tmp/{}'.format(filename)
    if put(archive_path, remote_path).failed:
        return False

    dirname = '/data/web_static/releases/{}'.format(
        filename.replace('.tgz', ''))
    if run('mkdir -p {}'.format(dirname)).failed:
        return False

    if run('tar -xzf {} -C {}'.format(remote_path, dirname)).failed  run('rm current')
        run('ln -s {} current'.format(dirname))

    return True


def deploy():
    """
    Full deployment of the web application.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """
    Remove old archives from the local and remote machines.

    Args:
        number: The number of archives to keep (0 means keep all).
    """
    number = int(number)
    if number < 1:
        number = 1

    with lcd('versions'):
        archives = local('ls -t web_static*.tgz', capture=True)
        if len(archives) == 0:
            return
        archives = archives.split('\n')[:-number]
        for archive in archives:
            local('rm -f {}'.format(archive))

    with cd('/data/web_static/releases'):
        releases = run('ls -t').split()
        if len(releases) == 0:
            return
        releases = releases[:-number]
        for release in releases:
            if release != 'test':
                run('rm -rf {}'.format(release))

