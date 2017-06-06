# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_delete_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('biografia', ckeditor.fields.RichTextField(blank=True, help_text='Biografia del Perfil', verbose_name='biografia')),
                ('direccion', models.CharField(max_length=300, verbose_name='direccion')),
                ('estado', models.CharField(max_length=300, verbose_name='estado')),
                ('profesion', models.CharField(max_length=300, verbose_name='profesion')),
                ('trabajo', models.CharField(max_length=300, verbose_name='trabajo')),
                ('telefono', models.CharField(max_length=300, verbose_name='telefono')),
                ('correo', models.CharField(max_length=300, verbose_name='correo')),
                ('facebook', models.CharField(max_length=300, verbose_name='redes sociales')),
                ('twitter', models.CharField(max_length=300, verbose_name='redes sociales')),
                ('area_agricola', models.CharField(max_length=300, verbose_name='actividad agricola')),
                ('avatar', models.FileField(upload_to='static/avatar/')),
                ('subido_el', models.DateTimeField(verbose_name='actualizado el', auto_now_add=True)),
            ],
        ),
    ]
