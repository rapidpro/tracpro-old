from __future__ import unicode_literals

from dash.orgs.models import Org
from django.contrib.auth.models import User, Group
from django.test import TestCase
from tracpro.supervisors.models import Supervisor


class TracProTest(TestCase):
    """
    Base class for all test cases in TracPro
    """
    def setUp(self):
        self.superuser = User.objects.create_superuser(username="super", email="super@user.com", password="super")

        self.user = self.create_user("bob", extra_fields=dict(first_name="Bob"))

        self.org = Org.objects.create(name="UNICEF", timezone="Africa/Kigali",
                                      created_by=self.user, modified_by=self.user)
        self.supervisor = Supervisor.create(self.org, self.user, "Kigali")

    def create_user(self, username, group_names=(), extra_fields=None):
        user = User.objects.create_user(username, "%s@nyaruka.com" % username, **extra_fields)
        user.set_password(username)
        user.save()
        for group in group_names:
            user.groups.add(Group.objects.get(name=group))
        return user

    def login(self, user):
        self.assertTrue(self.client.login(username=user.username, password=user.username), "Couldn't login as %(user)s / %(user)s" % dict(user=user.username))

    def assertNoFormErrors(self, response, post_data=None):
        if response.status_code == 200 and 'form' in response.context:
            form = response.context['form']

            if not form.is_valid():
                errors = []
                for k, v in form.errors.iteritems():
                    errors.append("%s=%s" % (k,v.as_text()))
                self.fail("Create failed with form errors: %s, Posted: %s" % (",".join(errors), post_data))

