from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.forms import ModelForm, fields, widgets
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *
username_validator = UnicodeUsernameValidator()
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class Aplly(forms.ModelForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={
        "class":"required form-control",
        "id":"fname",
        "name":"fname",
        "placeholder":"First Name *"
        }))

    last_name= forms.CharField(widget=forms.TextInput(attrs={
        "class":"required form-control",
        "id":"lname",
        "name":"lname",
        "placeholder":"Last Name *"
        }))
    email= forms.CharField(widget=forms.EmailInput(attrs={
        "class":"required form-control h5-email",
        "id":"contactEmail",
        "name":"contactEmail",
        "placeholder":"Email *"
        }))
    
    why= forms.CharField(widget=forms.Textarea(attrs={
        "class":"required form-control",
        "id":"comment",
        "name":"comment",
        "placeholder":"Type your message here *"
        }))

    place_living=forms.CharField(widget=forms.TextInput(attrs={
        "class":"required form-control",
        "id":"fplace",
        "name":"fplace",
        "placeholder":"Where do you live? *"
        }))
    major_of_study=forms.CharField(widget=forms.TextInput(attrs={
        "class":"required form-control",
        "id":"fstudy",
        "name":"fstudy",
        "placeholder":"Which major do you study? *"
        }))
    year_of_study=forms.CharField(widget=forms.TextInput(attrs={
        "class":"required form-control",
        "id":"fstudy",
        "name":"fstudy",
        "placeholder":"Which year you are in ? *"
        }))
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={
        "class":"required form-control","id":"contactPhone","placeholder":"Phone number "})
        )
    

    class Meta:
        model=ApplicationFormBootcamp
        fields=["first_name","last_name","email","why","place_living","major_of_study","year_of_study","phone_number"]



class Contact(forms.ModelForm):
    first_name= forms.CharField(widget=forms.TextInput(attrs={
        "class":"required form-control",
        "id":"fname",
        "name":"fname",
        "placeholder":"First Name *"
        }))

    last_name= forms.CharField(widget=forms.TextInput(attrs={
        "class":"required form-control",
        "id":"lname",
        "name":"lname",
        "placeholder":"Last Name *"
        }))
    email= forms.CharField(widget=forms.EmailInput(attrs={
        "class":"required form-control h5-email",
        "id":"contactEmail",
        "name":"contactEmail",
        "placeholder":"Email *"
        }))
    
    query= forms.CharField(widget=forms.Textarea(attrs={
        "class":"required form-control",
        "id":"comment",
        "name":"comment",
        "placeholder":"Type your message here *"
        }))

    
    

    class Meta:
        model=ContactUs
        fields=["first_name","last_name","email","query"]