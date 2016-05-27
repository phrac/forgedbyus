web: gunicorn forgedbyus.wsgi --log-file -
worker: celery worker -A forgedbyus worker -E -B --loglevel=INFO
