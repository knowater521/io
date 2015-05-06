from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Article

def Index(req):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render_to_response('index.html', context)

def Works(req):
    context = {'title': 'sfsdxxxxf'}
    return render_to_response('works.html', context)

def About(req):
    context = {'title': 'sfsdxxxxf'}
    return render_to_response('about.html', context)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'index.html'