# Generated by Django 4.2 on 2024-07-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Page', '0013_alter_technology_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='icon',
            field=models.FileField(upload_to='technology/'),
        ),
    ]