# Generated by Django 2.1 on 2019-03-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20190306_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='authenticator',
            field=models.CharField(max_length=64),
        ),
    ]
