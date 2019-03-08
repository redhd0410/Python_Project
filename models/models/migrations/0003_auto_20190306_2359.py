# Generated by Django 2.1 on 2019-03-06 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20190304_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authenticator',
            name='user_id',
        ),
        migrations.AddField(
            model_name='authenticator',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='models.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authenticator',
            name='authenticator',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=148),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='username', max_length=10),
        ),
    ]
