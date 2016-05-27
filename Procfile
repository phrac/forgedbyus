web: gunicorn forgedbyus.wsgi --log-file -
worker: celery worker -A forgedbyus -E -B --loglevel=INFO
