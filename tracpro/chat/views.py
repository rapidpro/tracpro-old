from dash.orgs.views import OrgPermsMixin
from smartmin.views import SmartTemplateView
from .models import lookup_chat_messages

class ChatListView(OrgPermsMixin, SmartTemplateView):
    template_name = 'chat/chat_list.html'
    permission = 'orgs.org_chat_list'

    def get_context_data(self, **kwargs):
        context = super(ChatListView, self).get_context_data(**kwargs)
        context['msgs'] = lookup_chat_messages(self.request.org)
        return context
