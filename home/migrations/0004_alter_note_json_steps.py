# Generated by Django 3.2.9 on 2022-01-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220119_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='json_steps',
            field=models.TextField(blank=True, default='[]'),
        ),
    ]
