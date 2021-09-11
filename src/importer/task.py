from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from importer.import_csv import ImportCsv
import logging
from celery import shared_task

logger = logging.getLogger(__name__)


@task(bind=True, name="import_csv_async", default_retry_delay=60, retry_kwargs={'max_retries': 3}, queue="csv_queue")
def import_csv_async(self):
    """sends an email """
    try :
        logger.info('### Scheduler started ###')
        import_obj = ImportCsv()
        import_obj.import_csv_to_db()
    except Exception as exc:
        logger.exception('Celery task failure!!!1', exc_info=exc)
        raise self.retry(exc=exc, countdown=60)


@shared_task(name = "print_msg_main")
def print_message(*args, **kwargs):
  print(f"Celery is working!! Message is Hewllo")





