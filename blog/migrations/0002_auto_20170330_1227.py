# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-30 18:27
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='contenido',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Contenido de la página', verbose_name='Contenido'),
        ),
    ]