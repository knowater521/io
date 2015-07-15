from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^article/(?P<slug>\S+)/$', views.ArticleDetail.as_view(), name='article'),
    url(r'^category/(?P<slug>[-\w]+)/$', views.CategoryHome, name='category_home'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.TagHome, name='tag_home'),
    url(r'^$', views.Index, name='index'),
    url(r'^archives/', views.Archives, name='archives'),
    url(r'^works/', views.Works, name='works'),
    url(r'^about/', views.About, name='about'),
    url(r'^book/', views.Book, name='book'),
    url(r'^activity/', views.Activity, name='activity'),
    url(r'^', views.Index, name='index'),
)
