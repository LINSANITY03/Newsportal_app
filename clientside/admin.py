from django.contrib import admin
from .models import News, News_category

# Register your models here.
admin.site.register(News_category)
admin.site.register(News)
