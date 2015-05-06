from django.conf.urls import url
from . import views

urlpatterns = (
    #url(r'^article/(?P<id>\S+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^$', views.Index, name='index'),
    url(r'^works/', views.Works, name='works'),
    url(r'^about/', views.About, name='about'),
)