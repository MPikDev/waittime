# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2021-02-11 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_part', '0002_auto_20210128_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfoEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=48)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('open_time', models.TimeField(blank=True)),
                ('close_time', models.TimeField(blank=True)),
                ('address', models.CharField(max_length=128)),
                ('state', models.CharField(choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], default='WA', max_length=2)),
                ('city', models.CharField(max_length=128)),
                ('zip_code', models.IntegerField(blank=True)),
                ('wait_time', models.FloatField(blank=True)),
                ('load_time', models.FloatField(blank=True)),
                ('overnight_parking', models.BooleanField(default=False)),
                ('lumper', models.BooleanField(default=False)),
                ('facilities', models.BooleanField(default=False)),
                ('scheduling', models.CharField(choices=[('AP', 'Appointment'), ('FC', 'FCFS')], default='AP', max_length=2)),
                ('load_type', models.CharField(choices=[('PE', 'Perishable'), ('DR', 'Dry'), ('BO', 'Both')], default='PE', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='close_time',
            field=models.TimeField(blank=True, default='15:00'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='facilities',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='load_type',
            field=models.CharField(choices=[('PE', 'Perishable'), ('DR', 'Dry'), ('BO', 'Both')], default='PE', max_length=2),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='lumper',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='open_time',
            field=models.TimeField(blank=True, default='8:00'),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='overnight_parking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='scheduling',
            field=models.CharField(choices=[('AP', 'Appointment'), ('FC', 'FCFS')], default='AP', max_length=2),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='state',
            field=models.CharField(choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], default='WA', max_length=2),
        ),
    ]
