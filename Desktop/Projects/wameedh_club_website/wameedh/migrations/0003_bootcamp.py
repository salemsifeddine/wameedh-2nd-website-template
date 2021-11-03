# Generated by Django 3.2.8 on 2021-11-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wameedh', '0002_auto_20211030_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='BootCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=8000)),
                ('imageBackground', models.ImageField(upload_to='events')),
                ('imageEvent', models.ImageField(upload_to='eventsImage')),
            ],
        ),
    ]