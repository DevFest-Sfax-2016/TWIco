# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexe', models.CharField(choices=[('H', 'Homme'), ('F', 'Famme')], max_length=1)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('searchFor', models.CharField(choices=[('H', 'Homme'), ('F', 'Famme')], max_length=1)),
                ('mail', models.EmailField(max_length=254)),
                ('pays', models.CharField(max_length=40)),
                ('birthday', models.DateField()),
            ],
        ),
    ]