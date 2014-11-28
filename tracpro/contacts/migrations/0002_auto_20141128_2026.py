# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='urn',
        ),
        migrations.AddField(
            model_name='contact',
            name='urn_path',
            field=models.CharField(default='', max_length=255, verbose_name='URN Path'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='urn_scheme',
            field=models.CharField(default='tel', max_length=255, verbose_name='URN Scheme'),
            preserve_default=True,
        ),
    ]
