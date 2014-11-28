from __future__ import unicode_literals

from tracpro.test import TracProTest


class SupervisorTest(TracProTest):
    def test_model(self):
        self.assertEqual("Bob", self.supervisor.get_name())
        self.assertEqual(self.kandahar, self.supervisor.get_region())

        self.assertIsNone(self.superuser.get_region())  # not a supervisor


class SupervisorCRUDLTest(TracProTest):
    def test_create(self):
        self.login(self.superuser)

        # TODO