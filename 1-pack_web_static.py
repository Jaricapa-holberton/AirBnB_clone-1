#!/usr/bin/python3
"""Define the task to_pack to fabric (fab) command"""

from fabric.api import *
from datetime import datetime
# get the actual time at the exceution moment
now = datetime.now()


# create a compressed file with the do_pack function
def do_pack():
    """Generate a .tgz archive from the contents of the web_static."""

    # format the name of the file with the timestamps
    now_year = now.year
    now_month = now.month
    now_day = now.day
    now_hour = now.hour
    now_minute = now.minute
    now_second = now.second
    # apply the format
    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        now_year, now_month, now_day, now_hour, now_minute, now_second
    )
    # All archives must be stored in the folder versions
    local('mkdir -p versions')
    # execute locally the compression of the folder
    command = local("tar -cvzf " + file_name + " ./web_static/")
    # return the archive path if the archive has been correctly generated
    if command.succeeded:
        return file_name
    else:
        return None
