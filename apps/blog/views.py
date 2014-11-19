from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render_to_response('blog/home.html')