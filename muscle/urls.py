from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^board/', include('muscle.board.urls', namespace='board')),
    url(r'', include('muscle.core.urls', namespace='core')),
)
