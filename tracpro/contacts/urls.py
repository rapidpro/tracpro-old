from __future__ import unicode_literals

from django.conf.urls import patterns, url
from .views import ContactListView

urlpatterns = patterns('',
    url(r'^contacts/', ContactListView.as_view(), name='contacts.contact_list')
)