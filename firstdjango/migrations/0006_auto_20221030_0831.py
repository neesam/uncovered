# Generated by Django 2.2.4 on 2022-10-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstdjango', '0005_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='artist',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='records',
            name='title',
            field=models.TextField(max_length=500),
        ),
    ]