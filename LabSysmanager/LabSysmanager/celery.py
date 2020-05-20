# LabSysmanager/celery.py

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LabSysmanager.settings')

app = Celery('LabSysmanager')
app.config_from_object('django.conf:settings')
app.conf.timezone = 'America/Sao_Paulo'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'core.tasks.populate_task',
        'schedule': crontab(minute='*/20'),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}