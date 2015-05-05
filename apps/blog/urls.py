from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.Index, name='index'),
    url(r'^works/', views.Works, name='works'),
    url(r'^about/', views.About, name='about'),
)