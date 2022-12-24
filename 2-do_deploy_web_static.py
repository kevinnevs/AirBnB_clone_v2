#!/usr/bin/python3
"""
Fabricp script that distributes archive to web servers
using function do_deploy
"""
from fabric.api import env, put, run, local
import os.path
env.hosts = ['18.209.225.104', '100.26.209.134']

def do_deploy(archive_path):
    """
    Deploy archive to the web server
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        release_dir = "/data/web_static/releases/{}".format(file_name.split(".")[0])

        # upload archive to server
        put(archive_path, "/tmp/{}".format(file_name))

        # create release directory
        run("mkdir -p {}".format(release_dir))

        # uncompress archive
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_dir))

        # remove archive
        run("rm /tmp/{}".format(file_name))

        # move files to release directory
        run("mv {}web_static/* {}".format(release_dir, release_dir))

        # remove web_static directory
        run("rm -rf {}web_static".format(release_dir))

        # delete current symlink
        run("rm -rf /data/web_static/current")

        # create new symlink to release directory
        run("ln -s {} /data/web_static/current".format(release_dir))
        return True
    except:
        return False
