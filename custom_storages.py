from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ To store static files """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ To store Media files """
    location = settings.MEDIAFILES_LOCATION
