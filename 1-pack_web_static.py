#!/usr/bin/python3
"""
Fabric script that generates a .tgz archivefrom the contents of web_static
folder of AirBnB clone repo, using function do-pack
"""
from time import strftime
from fabric.api import local


def do_pack():
    """try loop definition of function"""
    timenow = strftime("%Y%m%d%H%M%S")
    try:
       local('mkdir -p versions')
       file_name = "versions/web_static_{}.tgz".format(timenow)
       local("tar -cvzf {} web_static/".format(file_name))
       return file_name
    except:
       return None
