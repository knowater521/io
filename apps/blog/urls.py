from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'apps.blog.views.article', name='blog.article'),
    url(r'^toolkit/', 'apps.blog.views.toolkit', name='blog.toolkit'),
    url(r'^works/', 'apps.blog.views.works', name='blog.works'),
    url(r'^about/', 'apps.blog.views.about', name='blog.about'),
)
