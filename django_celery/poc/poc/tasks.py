from __future__ import absolute_import
from celery import shared_task
from celery.exceptions import Reject
import time


@shared_task(bind=True, acks_late=True)
def gerar_relatorio(self):

    print('Started task, processing...')
    time.sleep(120)

    try:
        3/0
    except Exception as ex:
        raise Reject(requeue=True)

    print('Finished Task')

    return True
