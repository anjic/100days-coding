from django.core.management.base import BaseCommand
import os
import subprocess
import time

from xio_ise.settings import BASE_DIR

class Command(BaseCommand):
    """
    """
    def handle(self, *args, **options):             
        time.sleep(3)
        subprocess.Popen("python %s publisher"%(os.path.join(BASE_DIR,'manage.py')),shell=True)
        subprocess.Popen("python %s subscriber"%(os.path.join(BASE_DIR,'manage.py')),shell=True)
        subprocess.Popen("python %s collector"%(os.path.join(BASE_DIR,'manage.py')),shell=True)
        subprocess.Popen("python %s aggregator"%(os.path.join(BASE_DIR,'manage.py')),shell=True)
        subprocess.Popen("python %s logs"%(os.path.join(BASE_DIR,'manage.py')),shell=True)
        subprocess.Popen("python %s alert_mail"%(os.path.join(BASE_DIR,'manage.py')),shell=True)
        subprocess.Popen("python %s db_sync"%(os.path.join(BASE_DIR,'manage.py')),shell=True)
        subprocess.Popen("python %s mrc_status_sync"%(os.path.join(BASE_DIR,'manage.py')),shell=True)