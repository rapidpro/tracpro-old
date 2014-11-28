# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from uuid import uuid4


def populate_region(apps, schema_editor):
    Region = apps.get_model('contacts', 'region')
    Org = apps.get_model('orgs', 'org')
    Supervisor = apps.get_model('supervisors', 'supervisor')
    for supervisor in Supervisor.objects.all():
        region = Region.objects.filter(name=supervisor.region_old).first()
        if not region:
            org = Org.objects.get(editors=supervisor)
            region = Region.objects.create(group_uuid=uuid4(), name=supervisor.region_old, org=org)

        supervisor.region = region
        supervisor.save(update_fields=('region',))


class Migration(migrations.Migration):

    dependencies = [
        ('supervisors', '0002_auto_20141102_2231'),
        ('contacts', '__first__'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supervisor',
            old_name='region',
            new_name='region_old'
        ),
        migrations.AddField(
            model_name='supervisor',
            name='region',
            field=models.ForeignKey(verbose_name='Region',
                                    to='contacts.Region',
                                    null=True,
                                    help_text='The name of the region or state this supervisor belongs to'),
            preserve_default=True,
        ),
        migrations.RunPython(populate_region),
        migrations.AlterField(
            model_name='supervisor',
            name='region',
            field=models.ForeignKey(verbose_name='Region',
                                    to='contacts.Region',
                                    help_text='The name of the region or state this supervisor belongs to'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='region_old'
        ),
    ]
