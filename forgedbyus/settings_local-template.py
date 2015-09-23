### Amazon S3 Settings ###
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_ASSOCIATE_TAG = ''

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}

SECRET_KEY = 'YOUR SECRET KEY HERE'
