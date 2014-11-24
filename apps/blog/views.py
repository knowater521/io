from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

import os
from os.path import join
from xblog.settings import BASE_DIR


def article(req):
    return render_to_response(join(BASE_DIR, 'templates/blog/article.html'))

def toolkit(req):
    return render_to_response(join(BASE_DIR, 'templates/blog/toolkit.html'))

def works(req):
    return render_to_response(join(BASE_DIR, 'templates/blog/works.html'))

def about(req):
    return render_to_response(join(BASE_DIR, 'templates/blog/about.html'))