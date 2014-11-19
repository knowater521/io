from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'apps.home.views.index',),
)
