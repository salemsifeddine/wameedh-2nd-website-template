# Generated by Django 3.2.8 on 2021-11-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wameedh', '0003_bootcamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubevents',
            old_name='images',
            new_name='imageBackground',
        ),
        migrations.AddField(
            model_name='clubevents',
            name='imageEvent',
            field=models.ImageField(blank=True, upload_to='clubEventsImages'),
        ),
    ]
