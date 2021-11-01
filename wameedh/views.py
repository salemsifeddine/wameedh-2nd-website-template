from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import  redirect
from django.core.mail import send_mail, EmailMessage
import csv
from django.template.loader import get_template
from django.views import generic
from django.conf import settings
from django.urls import reverse
from django.views.generic.edit import FormMixin
# Create your views here.


def main(request):
    members=Members.objects.all()
    achievements=ClubAchivement.objects.all()
    events=ClubEvents.objects.all()
    aboutus=AboutUsInfo.objects.all()
    bootcamps=BootCamp.objects.all()

    context={"members":members,"achievements":achievements,"events":events,"aboutus":aboutus,
    "bootcamps":bootcamps}

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



class EventApplication(FormMixin,generic.DetailView):
    model=ClubEvents
    form_class=Aplly
    template_name="pages/apply.html"
    success_url = '/'
  


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
   

    
    
    def form_valid(self, form):
        print(self.kwargs["title"])
        email = form.cleaned_data["email"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        phonenumber = form.cleaned_data["phone_number"]
        place_living = form.cleaned_data["place_living"]
        major_of_study = form.cleaned_data["major_of_study"]
        year_of_study = form.cleaned_data["year_of_study"]
        why = form.cleaned_data["why"]

        edition=ClubEvents.objects.get(title=self.object.title).edition
        title=ClubEvents.objects.get(title=self.object.title).title

   

        with open("wameedh/static/data/applicationForm.csv","a",newline="") as f:
            writer = csv.writer(f)
            writer.writerow([first_name,last_name,email,phonenumber,place_living,
            major_of_study,year_of_study,why])
        f.close()
        context_data={
            "name":f"{first_name} - {last_name}",
            "edition":edition,
            "eventname":title
            }

        template=get_template("pages/applicationForm.html").render(context_data)
        msg=EmailMessage(
            "First Admition for Our next Event",
            template,
            "wameedh.sc@gmail.com",
            [email],
            # reply_to=["bootcamp"]
            )
                
        msg.content_subtype= 'html'
                
        msg.send(fail_silently=False)
        return super(EventApplication, self).form_valid(form)   


class BootCampApplication(FormMixin,generic.DetailView):
    
    model=BootCamp
    form_class=Aplly
    template_name="pages/apply.html"
    success_url = '/'


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        phonenumber = form.cleaned_data["phone_number"]
        place_living = form.cleaned_data["place_living"]
        major_of_study = form.cleaned_data["major_of_study"]
        year_of_study = form.cleaned_data["year_of_study"]
        why = form.cleaned_data["why"]

        edition=BootCamp.objects.get(title=self.object.title).edition
        title=BootCamp.objects.get(title=self.object.title).title

        with open("wameedh/static/data/applicationForm.csv","a",newline="") as f:
            writer = csv.writer(f)
            writer.writerow([first_name,last_name,email,phonenumber,place_living,
            major_of_study,year_of_study,why])
        f.close()

        context_data={
            "name":f"{first_name} {last_name}",
            "edition":edition,
            "eventname":title
            }

        template=get_template("pages/applicationForm.html").render(context_data)
        msg=EmailMessage(
            "First Admition for Our Next Bootcamp",
            # template,
            template,
            "wameedh.sc@gmail.com",
            [email],
            # reply_to=["bootcamp"]
            )
                
        msg.content_subtype= 'html'
                
        msg.send(fail_silently=False)
        return super(BootCampApplication, self).form_valid(form)   
    


        

def application(request):

    return render(request,"pages/applicationForm.html")