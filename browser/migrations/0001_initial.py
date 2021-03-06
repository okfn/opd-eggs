# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 07:56
from __future__ import unicode_literals

import browser.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('BSIN', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('BRAND_NM', models.CharField(max_length=255)),
                ('BRAND_LINK', models.CharField(blank=True, max_length=255, null=True)),
                ('BRAND_OPEN', models.NullBooleanField(default=False)),
                ('BRAND_DISPLAY', models.NullBooleanField(default=True)),
            ],
            options={
                'ordering': ('BRAND_NM',),
            },
        ),
        migrations.CreateModel(
            name='Brand_type',
            fields=[
                ('BRAND_TYPE_CD', models.AutoField(primary_key=True, serialize=False)),
                ('BRAND_TYPE_NM', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CAT_CD', models.AutoField(primary_key=True, serialize=False)),
                ('CAT_NM', models.CharField(max_length=255)),
                ('CAT_LINK', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('COLOR_CD', models.AutoField(primary_key=True, serialize=False)),
                ('COLOR_NM', models.CharField(max_length=255)),
                ('COLOR_DESC', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('COUNTRY_ISO', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('COUNTRY_NM_U', models.CharField(max_length=80)),
                ('COUNTRY_NM_L', models.CharField(max_length=80)),
                ('COUNTRY_ISO3', models.CharField(max_length=3, null=True)),
            ],
            options={
                'ordering': ('COUNTRY_ISO',),
            },
        ),
        migrations.CreateModel(
            name='Fed',
            fields=[
                ('FED_CD', models.AutoField(primary_key=True, serialize=False)),
                ('FED_NM', models.CharField(max_length=255)),
                ('FED_DESC', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('GRADE_CD', models.AutoField(primary_key=True, serialize=False)),
                ('GRADE_NM', models.CharField(max_length=255)),
                ('GRADE_SHORT_NM', models.CharField(blank=True, max_length=255, null=True)),
                ('GRADE_DESC', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gs1_gcp',
            fields=[
                ('GCP_CD', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('GLN_CD', models.CharField(blank=True, max_length=13, null=True)),
                ('GLN_NM', models.CharField(blank=True, max_length=255, null=True)),
                ('GLN_ADDR_02', models.CharField(blank=True, max_length=38, null=True)),
                ('GLN_ADDR_03', models.CharField(blank=True, max_length=38, null=True)),
                ('GLN_ADDR_04', models.CharField(blank=True, max_length=38, null=True)),
                ('GLN_ADDR_POSTALCODE', models.CharField(blank=True, max_length=38, null=True)),
                ('GLN_ADDR_CITY', models.CharField(max_length=38)),
                ('GLN_COUNTRY_ISO_CD', models.CharField(max_length=38)),
                ('CONTACT_NAME', models.CharField(blank=True, max_length=38, null=True)),
                ('CONTACT_TEL', models.CharField(blank=True, max_length=255, null=True)),
                ('CONTACT_HOTLINE', models.CharField(blank=True, max_length=255, null=True)),
                ('CONTACT_FAX', models.CharField(blank=True, max_length=255, null=True)),
                ('CONTACT_MAIL', models.CharField(blank=True, max_length=255, null=True)),
                ('CONTACT_WEB', models.CharField(blank=True, max_length=255, null=True)),
                ('GLN_LAST_CHANGE', models.CharField(blank=True, max_length=10, null=True)),
                ('GLN_PROVIDER', models.CharField(blank=True, max_length=13, null=True)),
                ('SEARCH_GTIN_CD', models.CharField(blank=True, max_length=13, null=True)),
                ('GEPIR_GCP_CD', models.CharField(blank=True, max_length=13, null=True)),
                ('ADD_PARTY_ID', models.CharField(blank=True, max_length=13, null=True)),
                ('SOURCE', models.CharField(max_length=100)),
                ('SYNC_DT', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('GCP_CD',),
            },
        ),
        migrations.CreateModel(
            name='Gs1_gcp_rc',
            fields=[
                ('RETURN_CODE', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('RETURN_NAME', models.CharField(max_length=255)),
                ('ORIGIN', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gtin',
            fields=[
                ('GTIN_ID', django_extensions.db.fields.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('GTIN_CD', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 13', regex='^.{13}$')])),
                ('PKG_UNIT', models.IntegerField(blank=True, default=0, null=True)),
                ('BSIN', models.ForeignKey(default=browser.models.get_brand_default, on_delete=django.db.models.deletion.CASCADE, to='browser.Brand')),
                ('CAT_CD', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Category')),
                ('COLOR_CD', models.ForeignKey(blank=True, default=browser.models.get_color_default, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Color')),
                ('FED_CD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Fed')),
                ('GCP_CD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Gs1_gcp')),
                ('GRADE_CD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Grade')),
            ],
            options={
                'ordering': ('METHOD_CD', 'SIZE_CD', 'GTIN_CD'),
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('LABEL_CD', models.AutoField(primary_key=True, serialize=False)),
                ('LABEL_NM', models.CharField(max_length=255)),
                ('LABEL_DESC', models.TextField(blank=True, null=True)),
                ('LABEL_LINK', models.CharField(blank=True, max_length=255, null=True)),
                ('LABEL_COUNTRY_ISO', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Country')),
            ],
            options={
                'ordering': ('LABEL_COUNTRY_ISO', 'LABEL_NM'),
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('METHOD_CD', models.AutoField(primary_key=True, serialize=False)),
                ('METHOD_NM', models.CharField(max_length=255)),
                ('METHOD_DESC', models.TextField(blank=True, null=True)),
                ('METHOD_LEVEL_CD', models.IntegerField(blank=True, null=True)),
                ('METHOD_ISO', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Country')),
            ],
            options={
                'ordering': ('METHOD_ISO', 'METHOD_NM'),
            },
        ),
        migrations.CreateModel(
            name='Orga',
            fields=[
                ('ORGA_CD', models.AutoField(primary_key=True, serialize=False)),
                ('ORGA_NM', models.CharField(blank=True, max_length=255, null=True)),
                ('ORGA_LINK', models.CharField(blank=True, max_length=255, null=True)),
                ('ORGA_WIKI_EN', models.CharField(blank=True, max_length=255, null=True)),
                ('ORGA_COUNTRY_ISO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Country')),
            ],
            options={
                'ordering': ('ORGA_NM',),
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('OWNER_CD', models.AutoField(primary_key=True, serialize=False)),
                ('OWNER_NM', models.CharField(blank=True, max_length=255, null=True)),
                ('OWNER_LINK', models.CharField(blank=True, max_length=255, null=True)),
                ('OWNER_WIKI_EN', models.CharField(blank=True, max_length=255, null=True)),
                ('OWNER_COUNTRY_ISO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Country')),
            ],
            options={
                'ordering': ('OWNER_NM',),
            },
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('PACKAGING_CD', models.AutoField(primary_key=True, serialize=False)),
                ('PACKAGING_NM', models.CharField(max_length=255)),
                ('PACKAGING_LINK', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('GTIN_CD', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('SEARCH_NB', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Search_api',
            fields=[
                ('GTIN_CD', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('SEARCH_NB', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('SIZE_CD', models.AutoField(primary_key=True, serialize=False)),
                ('SIZE_NM', models.CharField(max_length=255)),
                ('SIZE_SIZE_NM', models.CharField(blank=True, max_length=255, null=True)),
                ('SIZE_DESC', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('SIZE_NM',),
            },
        ),
        migrations.AddField(
            model_name='gtin',
            name='LABEL_CD',
            field=models.ManyToManyField(blank=True, to='browser.Label'),
        ),
        migrations.AddField(
            model_name='gtin',
            name='METHOD_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Method'),
        ),
        migrations.AddField(
            model_name='gtin',
            name='PACKAGING_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Packaging'),
        ),
        migrations.AddField(
            model_name='gtin',
            name='SIZE_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Size'),
        ),
        migrations.AddField(
            model_name='gs1_gcp',
            name='RETURN_CODE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Gs1_gcp_rc'),
        ),
        migrations.AddField(
            model_name='brand',
            name='BRAND_COUNTRY_ISO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Country'),
        ),
        migrations.AddField(
            model_name='brand',
            name='BRAND_TYPE_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Brand_type'),
        ),
        migrations.AddField(
            model_name='brand',
            name='OWNER_CD',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='browser.Owner'),
        ),
    ]
