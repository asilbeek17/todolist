# Generated by Django 4.2 on 2023-04-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='bowlaniwi',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
