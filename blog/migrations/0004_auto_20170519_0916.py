# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='documento',
            field=models.FileField(upload_to='static/documents/'),
        ),
    ]
