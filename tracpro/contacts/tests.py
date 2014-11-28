from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from tracpro.test import TracProTest


class ContactTest(TracProTest):
    # TODO
    pass


class ContactCRUDLTest(TracProTest):
    def test_list(self):
        list_url = reverse('contacts.contact_list')

        # log in as an administrator
        self.login(self.admin)

        # so should see contacts from all regions
        response = self.client_get(list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 3)

        # log in as a supervisor for Kandahar
        self.login(self.supervisor1)

        # so should see contacts from just Kandahar
        response = self.client_get(list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 2)

        # log in as administrator for different org with no contacts
        self.login(self.other_admin)
        response = self.client.get(list_url, HTTP_HOST='wfp.localhost')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 0)
