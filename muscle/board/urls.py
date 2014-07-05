# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('muscle.board.views',
    url(r'^statistics/$', 'statistics', name='board'),
    url(r'^search/$', 'search', name='board'),
    url(r'^startDB/$', 'startDB', name='board'),
    url(r'', 'home', name='board'),
)
