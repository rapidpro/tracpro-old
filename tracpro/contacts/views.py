from dash.orgs.views import OrgPermsMixin
from smartmin.views import SmartTemplateView

class ContactListView(OrgPermsMixin, SmartTemplateView):
    template_name = 'contacts/contact_list.html'
    permission = 'orgs.org_contact_list'

    def get_context_data(self, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        context['group'] = "%s" % self.request.user.get_region()
        context['contacts'] = self.request.org.get_api().get_contacts(group=context['group'])
        return context

