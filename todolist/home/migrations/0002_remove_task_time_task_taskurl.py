# Generated by Django 4.1.7 on 2023-03-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='time',
        ),
        migrations.AddField(
            model_name='task',
            name='taskUrl',
            field=models.TextField(default='#'),
        ),
    ]
