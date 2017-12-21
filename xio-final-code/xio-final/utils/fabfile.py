import os
from fabric.api import run, get, put, hide

def backup():
    with hide('output'):
        run('dbutils.sh -c')
        res = run('dbutils.sh -b')
        if res.return_code == 1:
            raise SystemExit()
        get('/tmp/xio_ise.zip', './ise_backup.zip')
        run('dbutils.sh -c')

def restore():
    if not os.path.isfile('./ise_backup.zip'):
        print 'Restore file not found on local machine'
        return
    with hide('output'):
        run('dbutils.sh -c')
        put('./ise_backup.zip', '/tmp/xio_ise.zip')
        res = run('dbutils.sh -r')
        if res.return_code == 1:
            raise SystemExit()
        run('dbutils.sh -c')