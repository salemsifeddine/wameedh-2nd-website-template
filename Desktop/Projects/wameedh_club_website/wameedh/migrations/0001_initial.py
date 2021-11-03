# Generated by Django 3.2.8 on 2021-10-30 16:19

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='aboutImages')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationFormBootcamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('place_living', models.CharField(max_length=50)),
                ('major_of_study', models.CharField(max_length=50)),
                ('year_of_study', models.CharField(max_length=50)),
                ('why', models.TextField(max_length=5000)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='ClubAchivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('images', models.ImageField(blank=True, upload_to='clubAchivemetns')),
            ],
        ),
        migrations.CreateModel(
            name='ClubEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('images', models.ImageField(blank=True, upload_to='clubEvents')),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(null=True, upload_to='members_images')),
            ],
        ),
    ]