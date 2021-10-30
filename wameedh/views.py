from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import  redirect
from django.core.mail import send_mail, EmailMessage
import csv
# Create your views here.


def main(request):
    members=Members.objects.all()
    achievements=ClubAchivement.objects.all()
    events=ClubEvents.objects.all()
    aboutus=AboutUsInfo.objects.all()

    context={"members":members,"achievements":achievements,"events":events,"aboutus":aboutus}

    return render(request, "pages/main.html",context)

# def earth(request):
#     context={}
#     return render(request, "pages/index.html",context)

def contactUs(request):
    if request.method != "POST":
        form = Contact()
     
    else:
        form= Contact(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            query = form.cleaned_data["query"]
            with open("wameedh\static\data\contact.csv","a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow([first_name,last_name,email,query])
            file.close()
            #    template=get_template("pages/applicationbootcamp.html").render(context_data)
            msg=EmailMessage(
            "EZORA MARKET E-commerce Site",
            # template,
            "thank u",
            "wameedh.sc@gmail.com",
            ["salemsifeddine1@gmail.com"],
            # reply_to=["bootcamp"]
            )
            
            msg.content_subtype= 'html'
            
            msg.send(fail_silently=False)
            return redirect("home")

    return render(request,"pages/contactus.html",{"forms":form})

def gallery(request):

    return render(request,"pages/gallery.html",{})

def projects(request):
    return render(request,"pages/projects.html",{})

def team(request):
    return render(request,"pages/team.html",{})

def apply(request):
   
    if request.method != "POST":
        form = Aplly()
     
    else:
        form= Aplly(request.POST)
        if form.is_valid():
            form.save()

            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phonenumber = form.cleaned_data["phone_number"]
            place_living = form.cleaned_data["place_living"]
            major_of_study = form.cleaned_data["major_of_study"]
            year_of_study = form.cleaned_data["year_of_study"]
            why = form.cleaned_data["why"]

            with open("wameedh/static/data/applicationForm.csv","a",newline="") as f:
                writer = csv.writer(f)
                writer.writerow([first_name,last_name,email,phonenumber,place_living,
                major_of_study,year_of_study,why])
            f.close()

            #    template=get_template("pages/applicationbootcamp.html").render(context_data)
            msg=EmailMessage(
            "EZORA MARKET E-commerce Site",
            # template,
            "thank u",
            "wameedh.sc@gmail.com",
            ["salemsifeddine1@gmail.com"],
            # reply_to=["bootcamp"]
            )
            
            msg.content_subtype= 'html'
            
            msg.send(fail_silently=False)
            return redirect("home")

    return render(request,"pages/apply.html",{"forms":form})