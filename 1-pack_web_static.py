#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB 
Clone repo, using the function do_pack
"""
from fabric.api import *
from datetime import datetime

env.arc_src = ''
env.arc_name = 'web_static_.tgz'
env.hosts = ['34.74.94.56', '34.74.11.212']
# User name and password should prferably be based
# as environmnt variables rather than explicitly typing them
# here 

def do_pack():
    """ Packages soruce code into a compressed archive
    """
    global env.arc_name

    now = datetime.now()
    tstr = now.strftime("%Y%m%d%H%M%S")
    env.arc_name = 'web_static_{}.tgz'.format(tstr)
    local("tar -cvzf %s %s" % (env.arc_name, env.arc_src), capture=False)

    try:
        with local("mkdir -p versions"):
            with local("cd versions"):
                local("cp ../%s ./" %(env.arc_name), capture=False)
        return env.arc_src+"/versions/{}".format(env.arc_name)
    except:
        return None

def do_deploy(archive_path):
    """Deploys a achive to a number of remote hosts
    """ 
    
    
