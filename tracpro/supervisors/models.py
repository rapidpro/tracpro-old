from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from tracpro.contacts.models import Region
from tracpro.utils import get_cacheable_attr


class Supervisor(User):
    """
    A Supervisor represents a supervisor for a particular region of a country. They are tied to a group of users
    and can view and manage results, chats etc.. in that region
    """
    region = models.ForeignKey(Region,
                               verbose_name=_("Region"),
                               help_text=_("The name of the region or state this supervisor belongs to"))

    @classmethod
    def create(cls, org, user, region):
        supervisor = Supervisor(user_ptr_id=user.pk)
        supervisor.__dict__.update(user.__dict__)
        supervisor.pk = None
        supervisor.region = region
        supervisor.save()
        supervisor.set_org(org)
        return supervisor

    def set_org(self, org):
        # remove ourselves as editor of other orgs, and add ourselves as an editor to this org
        self.org_editors.clear()
        self.org_editors.add(org)

    def get_name(self):
        return " ".join([part for part in (self.first_name, self.last_name) if part])

    def __unicode__(self):
        return self.get_name()

    class Meta:
        verbose_name = _("Supervisor")
        verbose_name_plural = _("Supervisors")


def get_region(user):
    """
    Gets the region for the given user if it's actually a supervisor
    """
    if isinstance(user, Supervisor):
        return user.region

    def calculate():
        supervisor = Supervisor.objects.filter(user_ptr_id=user.pk).first()
        return supervisor.region if supervisor else None

    return get_cacheable_attr(user, '__region', calculate)

# monkey patch onto user model
User.get_region = get_region


