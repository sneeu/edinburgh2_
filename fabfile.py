from fabric.api import *
from fabric.context_managers import cd


env.hosts = ['papa.sneeu.net']


def pull():
    with cd('/var/www/edinburgh2/'):
        run('git pull')
