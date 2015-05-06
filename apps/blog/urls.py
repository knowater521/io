from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^article/(?P<slug>\S+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^$', views.Index, name='index'),
    url(r'^works/', views.Works, name='works'),
    url(r'^about/', views.About, name='about'),
    url(r'^', views.Index, name='index'),
)