from django.db import models
from django.core.validators import RegexValidator
from django.forms.formsets import INITIAL_FORM_COUNT
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Members(models.Model):
    name=models.CharField(max_length=30)
    position=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    photo=models.ImageField(upload_to="members_images", null=True)

    def __str__(self):
        return self.name

class ClubAchivement(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    images=models.ImageField(upload_to="clubAchivemetns" ,blank=True)

    def __str__(self):
        return self.title

class ClubEvents(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    images=models.ImageField(upload_to="clubEvents" ,blank=True)

    def __str__(self):
        return self.title
    

class AboutUsInfo(models.Model):
    description=models.TextField(null=True)
    image=models.ImageField(upload_to="aboutImages",null=True)

    def __str__(self):
        return "description"

class ApplicationFormBootcamp(models.Model):
    first_name=models.CharField(max_length=50);
    last_name=models.CharField(max_length=50);
    email=models.EmailField(max_length=50);
    place_living=models.CharField(max_length=50);
    major_of_study=models.CharField(max_length=50);
    year_of_study=models.CharField(max_length=50);
    why=models.TextField(max_length=5000);
    phone_number = PhoneNumberField(blank=True,)

class ContactUs(models.Model):
    first_name=models.CharField(max_length=50);
    last_name=models.CharField(max_length=50);
    email=models.EmailField(max_length=50);
    query=models.TextField(max_length=5000);
    

