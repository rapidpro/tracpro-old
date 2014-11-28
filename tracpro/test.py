from __future__ import unicode_literals

from dash.orgs.models import Org
from django.contrib.auth.models import User
from django.test import TestCase
from tracpro.contacts.models import Contact, Region
from tracpro.supervisors.models import Supervisor
from uuid import uuid4


class TracProTest(TestCase):
    """
    Base class for all test cases in TracPro
    """
    def setUp(self):
        self.superuser = User.objects.create_superuser(username="super", email="super@user.com", password="super")

        self.org = Org.objects.create(name="UNICEF", timezone="Asia/Kabul", subdomain="unicef",
                                      created_by=self.superuser, modified_by=self.superuser)
        self.other_org = Org.objects.create(name="WFP", timezone="Africa/Kigali", subdomain="wfp",
                                            created_by=self.superuser, modified_by=self.superuser)

        self.admin = self.create_user("admin", org=self.org, first_name="Adrian", last_name="Admin")
        self.org.administrators.add(self.admin)

        self.other_admin = self.create_user("other_admin", org=self.other_org)
        self.other_org.administrators.add(self.other_admin)

        self.region1 = self.create_region("Kandahar")
        self.region2 = self.create_region("Spinbaldak")

        self.user1 = self.create_user("sam", org=self.org, first_name="Super", last_name="Sam")
        self.supervisor1 = Supervisor.create(self.org, self.user1, self.region1)

        self.user2 = self.create_user("sue", org=self.org, first_name="Sue")
        self.supervisor2 = Supervisor.create(self.org, self.user2, self.region2)

        self.create_contact("Ann", "1234", self.region1)
        self.create_contact("Bob", "2345", self.region1)
        self.create_contact("Jim", "3456", self.region2)

    def create_user(self, username, org, **extra_fields):
        user = User.objects.create_user(username, "%s@nyaruka.com" % username, username, **extra_fields)
        if org:
            user.set_org(org)

        return user

    def create_region(self, name, org=None, group_uuid=None):
        if not group_uuid:
            group_uuid = uuid4()
        if not org:
            org = self.org

        return Region.objects.create(group_uuid=group_uuid, name=name, org=org)

    def create_contact(self, name, phone, region, uuid=None):
        if not uuid:
            uuid = uuid4()

        return Contact.create(name, 'tel', phone, region, uuid)

    def login(self, user):
        result = self.client.login(username=user.username, password=user.username)
        self.assertTrue(result, "Couldn't login as %(user)s / %(user)s" % dict(user=user.username))

    def client_get(self, url, **kwargs):
        kwargs.update(dict(HTTP_HOST='unicef.localhost'))
        return self.client.get(url, **kwargs)

    def assertNoFormErrors(self, response, post_data=None):
        if response.status_code == 200 and 'form' in response.context:
            form = response.context['form']

            if not form.is_valid():
                errors = []
                for k, v in form.errors.iteritems():
                    errors.append("%s=%s" % (k, v.as_text()))
                self.fail("Create failed with form errors: %s, Posted: %s" % (",".join(errors), post_data))

