from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django_mysql.models import SizedTextField

import datetime
# Create your models here.


class News_category(MPTTModel, models.Model):
    class Meta:
        db_table = 'News_category'

    title = models.CharField(max_length=50, null=False, blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self) -> str:
        return f"{self.title}"


class News(models.Model):
    class Meta:
        db_table = 'News'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(
        upload_to='photos/news', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextUploadingField(default=' ')
    date_uploaded = models.DateField(default=datetime.datetime.now)
    time_uploaded = models.TimeField(default=datetime.datetime.now)
    news_category = models.ForeignKey(
        News_category, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.title} - {self.news_category}"
