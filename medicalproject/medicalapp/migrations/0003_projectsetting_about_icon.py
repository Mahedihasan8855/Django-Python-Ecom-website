# Generated by Django 3.1.2 on 2020-10-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0002_projectsetting_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsetting',
            name='about_icon',
            field=models.ImageField(blank=True, null=True, upload_to='icon/'),
        ),
    ]
