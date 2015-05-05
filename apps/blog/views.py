from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

def Index(req):
    #articles = Article.objects.all()
    #return HttpResponse(articles)
    context = {'article': 'sfsdf'}
    return render(req, 'index.html', context)