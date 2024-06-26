# Generated by Django 4.2 on 2024-06-24 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website_Settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='favicon',
            field=models.FileField(upload_to='favicon/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.FileField(upload_to='logo/'),
        ),
    ]
