# Generated by Django 4.2 on 2024-07-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insights_Page', '0002_insights'),
    ]

    operations = [
        migrations.CreateModel(
            name='FutureWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('cover_photo', models.ImageField(upload_to='insights/')),
                ('desc', models.TextField()),
            ],
        ),
    ]
