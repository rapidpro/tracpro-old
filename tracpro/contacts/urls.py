from django.conf.urls import patterns, include, url
from .views import ContactListView

urlpatterns = patterns('',
    url(r'^contacts/', ContactListView.as_view(), name='contacts.contact_list')
)