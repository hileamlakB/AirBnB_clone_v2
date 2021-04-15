#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB 
Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime

#env.hosts = ['34.74.94.56', '34.74.11.212']
# User name and password should prferably be based
# as environmnt variables rather than explicitly typing them
# here 

def do_deploy(archive_path):
    """Deploys a achive to a number of remote hosts
    """ 

    try:
        path_stat = local("test -e {} && echo True ".format(archive_path), capture=True)
    except Exception:
        return False
    else:

        file_name = archive.path.split("/")[-1]
        folder_name = file_name.split(".")[0]

        put(archive_path, "/tmp/{}".format(file_name)
        run("mkdir -p {}".format(folder_name)
 
