#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None
