#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Define the task do_deploy to fabric (fab) command"""

from fabric.api import *
from os import path

env.hosts = ['35.243.138.187', '3.84.128.192']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distribute an archive to your web servers"""

    # Returns False if the file at the path archive_path doesn’t exist
    if not path.exists(archive_path):
        print("path not exist")
        return False
    # get the path of the compressed file in locall
    # upload the archive to the /tmp/ directory of the web server
    compress_file = put(archive_path, "/tmp/")
    if compress_file.failed:
        return False
    # preparate the folder for uncompression
    # get the file name witout the numbers
    file_name = archive_path[len("versions/"): -1 * len(".tgz")]
    # create the path to the archives
    dest_folder = '/data/web_static/releases/'
    create_folder = run('mkdir -p ' + dest_folder + file_name + '/')
    if create_folder.failed:
        return False
    # uncompress on the folder created
    # create the string of the command to execute the uncompress
    part1_command = 'tar -xzf /tmp/' + file_name + '.tgz'
    part2_command = ' -C /data/web_static/releases/' + file_name + '/'
    # execute on the server the command
    unpack = run(part1_command + part2_command)
    if unpack.failed:
        return False
    # after uncompress, delete the archive from the web server
    del_archive = run('rm /tmp/' + file_name + '.tgz')
    if del_archive.failed:
        return False
    # move files to the new direction for the new symbolic link
    move = run('mv /data/web_static/releases/' +
               file_name +
               '/web_static/* /data/web_static/releases/' +
               file_name +
               '/')
    if move.failed:
        return False
    # delete the old direction folder
    del_folder = run('rm -rf /data/web_static/releases/' +
                     file_name +
                     '/web_static')
    if del_folder.failed:
        return False
    # Delete the symbolic link /data/web_static/current from the web server
    del_slink = run('rm -rf /data/web_static/current')
    if del_slink.failed:
        return False
    # Create new symbolic link /data/web_static/current on the web server
    create_slink = run('ln -sf /data/web_static/releases/' +
                       file_name + '/' + ' /data/web_static/current')
    if create_slink.failed:
        return False
    # if every step was correct, return true
    return True
