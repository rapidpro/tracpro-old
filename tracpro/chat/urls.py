from __future__ import unicode_literals

from django.conf.urls import patterns, url
from .views import ChatListView

urlpatterns = patterns('',
    url(r'^chat/', ChatListView.as_view(), name='chats.chat_list')
)