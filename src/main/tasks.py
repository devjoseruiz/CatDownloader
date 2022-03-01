import logging
import requests as r
import uuid
from celery import shared_task
from django.conf import settings

DOWNLOAD_URL = "https://thecatapi.com/api/images/get?format=src&type=gif"


@shared_task
def download_kitten_image():
    try:
        response = r.get(DOWNLOAD_URL)
    except (requests.exceptions.Timeout, requests.exceptions.TooManyRedirects, requests.exceptions.RequestException) as err:
        logging.exception(err)
        return False

    try:
        file_extension = response.headers.get('Content-Type').split('/')[-1]

        file_name = settings.BASE_DIR / 'downloads' / \
            (str(uuid.uuid4()) + '.' + file_extension)

        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
    except Exception as err:
        logging.exception(err)
        return False

    return True
