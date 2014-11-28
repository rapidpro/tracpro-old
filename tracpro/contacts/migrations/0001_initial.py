# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0009_auto_20141125_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(max_length=36)),
                ('name', models.CharField(help_text='The name of this contact', max_length=128, verbose_name='Name', blank=True)),
                ('urn', models.CharField(help_text='The URN of this contact', max_length=255, verbose_name='URN')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_uuid', models.CharField(max_length=36)),
                ('name', models.CharField(help_text='The name of this region', max_length=128, verbose_name='Name', blank=True)),
                ('org', models.ForeignKey(related_name='regions', verbose_name='Organization', to='orgs.Org')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='region',
            field=models.ForeignKey(related_name='contacts', verbose_name='Region', to='contacts.Region', help_text='The name of the region or state this contact lives in'),
            preserve_default=True,
        ),
    ]
