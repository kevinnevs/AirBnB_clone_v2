#!usr/bin/python3
"""
Fabric script that generates a .tgz archivefrom the contents of web_static
folder of AirBnB clone repo, using function do-pack
"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """try loop definition of function"""
    try:
       local('mkdir -p versions')
       date = datetime.now().strftime("%Y%m%d%H%M%S")
       file_name = "web_static_{}.tgz".format(date)
       local("tar -cvzf versions/{} web_static".format(file_name))
       return "versions/{}".format(file_name)
    except:
       return None
