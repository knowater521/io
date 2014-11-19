from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

def article(req):
    return render_to_response('blog/article.html')

def toolkit(req):
    return render_to_response('blog/toolkit.html')

def works(req):
    return render_to_response('blog/works.html')

def about(req):
    return render_to_response('blog/about.html')