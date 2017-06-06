# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170519_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='imagen_pdf',
            field=models.FileField(upload_to='static/imagenes_pdf/', default=datetime.datetime(2017, 5, 19, 15, 18, 57, 168501, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
