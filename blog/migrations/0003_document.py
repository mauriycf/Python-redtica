# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170330_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=255, blank=True)),
                ('titulo', models.CharField(max_length=300)),
                ('documento', models.FileField(upload_to='documents/')),
                ('subido_el', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
