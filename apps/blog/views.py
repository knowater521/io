from django.shortcuts import render
from django.http import HttpResponse


def Index(req):
    return HttpResponse('hello world!')