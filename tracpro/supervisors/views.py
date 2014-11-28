from __future__ import unicode_literals

from dash.orgs.models import Org
from dash.orgs.views import OrgPermsMixin
from django import forms
from django.core.validators import MinLengthValidator
from django.utils.translation import ugettext_lazy as _
from smartmin.users.views import SmartCRUDL, SmartCreateView, SmartUpdateView, SmartListView
from .models import Supervisor


class SupervisorForm(forms.ModelForm):
    is_active = forms.BooleanField(label=_("Active"),
                                   help_text=_("Whether this user is active, disable to remove access"))

    first_name = forms.CharField(max_length=128,
                                 label=_("First Name"), help_text=_("The first name of the user"))

    last_name = forms.CharField(max_length=128,
                                label=_("Last Name"), help_text=_("The last name of the user"))

    email = forms.CharField(max_length=256,
                            label=_("Email"), help_text=_("The email address for the user"))

    new_password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8)], required=False,
                                   label=_("New Password"),
                                   help_text=_("The password used to log in (minimum of 8 characters, optional)"))

    password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8)],
                               label=_("Password"), help_text=_("The password used to log in (minimum of 8 characters)"))

    region = forms.CharField(max_length=128,
                             label=_("Region"), help_text=_("The name of the region they supervise"))

    org = forms.ModelChoiceField(queryset=Org.objects.filter(is_active=True).order_by('name'),
                                 label=_("Site"), help_text=_("The site this user is part of"))

    class Meta:
        model = Supervisor
        exclude = []


class SupervisorCRUDL(SmartCRUDL):
    model = Supervisor
    actions = ('create', 'list', 'update')

    class List(OrgPermsMixin, SmartListView):
        fields = ('name', 'username', 'org', 'region')

        def derive_queryset(self, **kwargs):
            return super(SupervisorCRUDL.List, self).derive_queryset(**kwargs).filter(org=self.request.user.get_org())

        def get_name(self, obj):
            return obj.get_name()

        def get_org(self, obj):
            return ", ".join([unicode(o) for o in obj.org_editors.all()])

    class Create(OrgPermsMixin, SmartCreateView):
        form_class = SupervisorForm
        fields = ('first_name', 'last_name', 'email', 'password', 'org', 'region')

        def pre_save(self, obj):
            obj = super(SupervisorCRUDL.Create, self).pre_save(obj)
            obj.username = obj.email
            obj.set_password(self.form.cleaned_data['password'])
            return obj

        def post_save(self, obj):
            obj = super(SupervisorCRUDL.Create, self).post_save(obj)
            obj.set_org(self.form.cleaned_data['org'])
            return obj

    class Update(OrgPermsMixin, SmartUpdateView):
        form_class = SupervisorForm
        fields = ('is_active', 'first_name', 'last_name', 'email', 'new_password', 'org', 'region')

        def derive_initial(self):
            initial = super(SupervisorCRUDL.Update, self).derive_initial()

            initial['org'] = self.object.org_editors.all().first()
            return initial

        def pre_save(self, obj):
            obj = super(SupervisorCRUDL.Update, self).pre_save(obj)
            obj.username = obj.email
            new_password = self.form.cleaned_data.get('new_password', "")
            if new_password:
                obj.set_password(new_password)
            return obj

        def post_save(self, obj):
            obj = super(SupervisorCRUDL.Update, self).post_save(obj)
            obj.set_org(self.form.cleaned_data['org'])
            return obj
