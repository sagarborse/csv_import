from celery.decorators import task
import logging

logger = logging.getLogger("custom_logger")


@task(bind=True, name="send_async_mail", default_retry_delay=60, retry_kwargs={'max_retries': 3}, queue="mail_queue")
def import_csv(self, data):
    """sends an email """
    try :
        mailer =  MailService(data)
        mailer.send()
        logger.info("Sent mail with celery %s", data)
        return 'email sent {}'.format(data)
    except Exception as exc:
        logger.exception('Celery task failure!!!1', exc_info=exc)
        raise self.retry(exc=exc, countdown=60)





