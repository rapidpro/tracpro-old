# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervisors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supervisor',
            options={'verbose_name': 'Supervisor', 'verbose_name_plural': 'Supervisors'},
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='region',
            field=models.CharField(help_text='The name of the Region or State this supervisor belongs to, this should map to the Contact group on RapidPro', max_length=64, verbose_name='Region'),
            preserve_default=True,
        ),
    ]
