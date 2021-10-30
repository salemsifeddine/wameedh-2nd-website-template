from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import  redirect
from django.core.mail import send_mail, EmailMessage
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

    return render(request,"pages/contactus.html",{})

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