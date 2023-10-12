from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django_mysql.models import SizedTextField
import datetime
# Create your models here.


class news_category(MPTTModel, models.Model):
    class Metea:
        db_table = 'news_category'

    title = models.CharField(max_length=50, null=False, blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self) -> str:
        return f"{self.title}"


class news(models.Model):
    class Meta:
        db_table = 'news'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(
        upload_to='photos/news', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    date_uploaded = models.DateField(default=datetime.datetime.now)
    time_uploaded = models.TimeField(default=datetime.datetime.now)
    news_category = models.ForeignKey(
        news_category, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.title} - {self.news_category}"
