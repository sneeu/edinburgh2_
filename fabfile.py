from fabric.api import *
from fabric.context_managers import cd


env.hosts = ['unst.sneeu.com']


def pull():
    with cd('/var/www/edinburgh2/'):
        run('git pull')
