from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpRequest, request
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as view
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
   
    path("", views.main, name="home"),
    path("contact",views.contactUs,name="contact"),
    path("gallery",views.gallery,name="gallery"),
    path("projects",views.projects,name="projects"),
    path("team",views.team,name="team"),
    path("application/",views.application,name="application"),
    path(r"apply/Events/<int:pk>/",views.EventApplication.as_view(),name="applyEvent"),
    path(r"apply/Bootcamps/<int:pk>/",views.BootCampApplication.as_view(),name="applyBootcamp"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
