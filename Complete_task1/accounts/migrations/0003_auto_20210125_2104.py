# Generated by Django 3.0 on 2021-01-25 15:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='file',
            field=models.FileField(blank=True, default=datetime.datetime(2021, 1, 25, 15, 34, 27, 904993, tzinfo=utc), upload_to='images/'),
            preserve_default=False,
        ),
    ]