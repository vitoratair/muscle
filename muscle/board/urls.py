# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('muscle.core.views',
    url(r'^search/$', 'search', name='board'),
)
