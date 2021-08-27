#!/usr/bin/python3
"""Define the task do_deploy to fabric (fab) command"""

from fabric.api import run, put, env
from os import path, exists

env.hosts = ['35.243.138.187', '3.84.128.192']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distribute an archive to your web servers"""

    # Returns False if the file at the path archive_path doesn’t exist
    if exists(archive_path) is False:
        return False
    filename_wo_ext = archive_path[9:34]
    filename_w_ext = archive_path[9:]
    input_path = "/data/web_static/releases/{}/".format(filename_wo_ext)

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(input_path))
        run("sudo tar -zxvf /tmp/{} -C {}".format(filename_w_ext, input_path))
        run("sudo rm -rf /tmp/{}".format(filename_w_ext))
        run("sudo mv -n {}/web_static/* {}".format(input_path, input_path))
        run("sudo rm -rf {}/web_static".format(input_path))
        run("sudo rm /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(input_path))
        return True

    except Exception:
        return False
