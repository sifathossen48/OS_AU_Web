# Generated by Django 4.2 on 2024-07-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0008_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='logo',
            field=models.FileField(upload_to='technology/'),
        ),
    ]
