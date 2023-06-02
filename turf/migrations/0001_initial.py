# Generated by Django 3.2.11 on 2023-05-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_turf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turf_id', models.CharField(max_length=90)),
                ('turf_name', models.CharField(max_length=90)),
                ('contact_no', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('working_hrs', models.CharField(max_length=90)),
                ('location', models.CharField(max_length=90)),
                ('fee', models.CharField(max_length=90)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media')),
                ('status', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'tbl_turf',
            },
        ),
    ]