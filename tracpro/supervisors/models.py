from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Supervisor(User):
    """
    A Supervisor represents a supervisor for a particular region of a country. They are tied to a group of users
    and can view and manage results, chats etc.. in that region
    """
    region = models.CharField(max_length=64,
                              verbose_name=_("Region"),
                              help_text=_("The name of the Region or State this supervisor belongs to, this should map to the Contact group on RapidPro"))

    def set_org(self, org):
        # clear our current editors
        self.org_editors.clear()

        # add ourself as an editor to our new org
        self.org_editors.add(org)


    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _("Supervisor")
        verbose_name_plural = _("Supervisors")


def get_region(user):
    region = getattr(user, '__region', None)

    if region is None:
        supervisor = Supervisor.objects.filter(username=user.username).first()
        if supervisor:
            region = supervisor.region
        else:
            region = ''

        user.__region = region

    # '' indicates a cached value of None
    if region == '':
        return None
    else:
        return region

# monkey patch onto user model
User.get_region = get_region


