# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bang', '0031_eventparticipation_screenshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='cameo_members',
            field=models.ManyToManyField(related_name='cameo_members', verbose_name='Cameos', to='bang.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='_cache_cameos_last_update',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='_cache_j_cameos',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
