from django.conf.urls import patterns, include, url
from .views import ChatListView

urlpatterns = patterns('',
    url(r'^chat/', ChatListView.as_view(), name='chats.chat_list')
)