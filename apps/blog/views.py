from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def Index(req):
    context = {'title': 'sfsdxxxxf'}
    return render(req, 'index.html', context)