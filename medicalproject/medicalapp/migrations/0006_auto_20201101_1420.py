# Generated by Django 3.1.2 on 2020-11-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0005_contactmessage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
