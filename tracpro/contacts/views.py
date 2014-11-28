from __future__ import unicode_literals

from dash.orgs.views import OrgPermsMixin
from smartmin.users.views import SmartCRUDL, SmartListView
from .models import Contact


class ContactCRUDL(SmartCRUDL):
    model = Contact
    actions = ('list',)

    class List(OrgPermsMixin, SmartListView):
        def derive_fields(self):
            region = self.request.user.get_region()
            if region:
                return 'name', 'urn_path'
            else:
                return 'region', 'name', 'urn_path'

        def get_context_data(self, **kwargs):
            context = super(ContactCRUDL.List, self).get_context_data(**kwargs)
            context['region'] = self.request.user.get_region()
            return context

        def get_queryset(self, **kwargs):
            org = self.request.user.get_org()

            qs = super(ContactCRUDL.List, self).get_queryset(**kwargs)
            qs = qs.filter(region__org=org)

            region = self.request.user.get_region()
            if region:
                qs = qs.filter(region=region)
            return qs
