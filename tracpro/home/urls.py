from __future__ import unicode_literals

from django.conf.urls import patterns, url
from .views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view())
)