from __future__ import unicode_literals

from django.contrib.auth.models import User
from tracpro.test import TracProTest
from tracpro.utils import get_cacheable_attr


class InitTest(TracProTest):

    def test_get_cacheable_attr(self):
        # and when cached value is a non-empty string
        calculate = lambda: User.objects.get(pk=self.user1.pk).last_name

        with self.assertNumQueries(1):
            self.assertEqual("Sam", get_cacheable_attr(self, '__attr1', calculate))
        with self.assertNumQueries(0):
            self.assertEqual("Sam", get_cacheable_attr(self, '__attr1', calculate))

        # and when cached value is an empty string
        calculate = lambda: User.objects.get(pk=self.user2.pk).last_name

        with self.assertNumQueries(1):
            self.assertEqual("", get_cacheable_attr(self, '__attr2', calculate))
        with self.assertNumQueries(0):
            self.assertEqual("", get_cacheable_attr(self, '__attr2', calculate))

        # and when cached value is None
        calculate = lambda: User.objects.filter(pk=123).first()

        with self.assertNumQueries(1):
            self.assertIsNone(get_cacheable_attr(self, '__attr3', calculate))
        with self.assertNumQueries(0):
            self.assertIsNone(get_cacheable_attr(self, '__attr3', calculate))
