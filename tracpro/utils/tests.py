from __future__ import unicode_literals

from django.contrib.auth.models import User
from tracpro.test import TracProTest
from tracpro.utils import get_cacheable_attr


class InitTest(TracProTest):

    def test_get_cacheable_attr(self):
        calculate = lambda: User.objects.get(pk=self.org.created_by_id).first_name

        with self.assertNumQueries(1):
            self.assertEqual("Bob", get_cacheable_attr(self.supervisor, '__attr1', calculate))
        with self.assertNumQueries(0):
            self.assertEqual("Bob", get_cacheable_attr(self.supervisor, '__attr1', calculate))

        # and when cached value is blank string
        calculate = lambda: User.objects.get(pk=self.org.created_by_id).last_name

        with self.assertNumQueries(1):
            self.assertEqual("", get_cacheable_attr(self.supervisor, '__attr2', calculate))
        with self.assertNumQueries(0):
            self.assertEqual("", get_cacheable_attr(self.supervisor, '__attr2', calculate))

        # and when cached value is None
        calculate = lambda: User.objects.filter(pk=123).first()

        with self.assertNumQueries(1):
            self.assertIsNone(get_cacheable_attr(self.supervisor, '__attr3', calculate))
        with self.assertNumQueries(0):
            self.assertIsNone(get_cacheable_attr(self.supervisor, '__attr3', calculate))
