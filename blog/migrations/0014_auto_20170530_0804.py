# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil_user',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('age', models.CharField(max_length=100, blank=True)),
                ('cellphone', models.CharField(max_length=100, blank=True)),
                ('address', models.CharField(max_length=100, blank=True)),
                ('job_info', models.CharField(max_length=100, blank=True)),
                ('education', models.CharField(max_length=100, blank=True)),
                ('biography', models.CharField(max_length=300, blank=True)),
                ('social_network', models.CharField(max_length=100, blank=True)),
                ('avatar_image', models.FileField(upload_to='static/avatar/', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='id_user',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
