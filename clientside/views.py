from django.shortcuts import render
from .models import News
# Create your views here.


def home(request):
    news_query = News.objects.all()
    context = {'news_query': news_query}
    return render(request, "home.html", context)
