from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Photo(models.Model):

    photo = ThumbnailerImageField(upload_to='photo', max_length=255)