# coding: utf-8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('muscle.board.views',
    url(r'^search/$', 'search', name='board'),
)
