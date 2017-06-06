# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='correo',
        ),
        migrations.AddField(
            model_name='perfil',
            name='email',
            field=models.CharField(default=datetime.datetime(2017, 5, 25, 19, 50, 4, 33001, tzinfo=utc), max_length=300, verbose_name='email'),
            preserve_default=False,
        ),
    ]
