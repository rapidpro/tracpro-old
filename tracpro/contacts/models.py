from __future__ import unicode_literals

from dash.orgs.models import Org
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Region(models.Model):
    """
    Corresponds to a RapidPro contact group
    """
    group_uuid = models.CharField(max_length=36)  # TODO needs added on Temba side

    name = models.CharField(verbose_name=_("Name"), max_length=128, blank=True,
                            help_text=_("The name of this region"))

    org = models.ForeignKey(Org, verbose_name=_("Organization"), related_name='regions')


class Contact(models.Model):
    """
    Corresponds to a RapidPro contact
    """
    uuid = models.CharField(max_length=36)

    name = models.CharField(verbose_name=_("Name"), max_length=128, blank=True,
                            help_text=_("The name of this contact"))

    urn = models.CharField(verbose_name=_("URN"), max_length=255, help_text=_("The URN of this contact"))

    region = models.ForeignKey(Region,
                               verbose_name=_("Region"),
                               related_name='contacts',
                               help_text=_("The name of the region or state this contact lives in"))

    def get_responses(self):
        return self.responses.order_by('-created_on')

    def get_last_answer(self, question):
        from tracpro.polls.models import PollAnswer
        return PollAnswer.objects.filter(question=question, reponse__contact=self).order_by('-submitted_on').first()
