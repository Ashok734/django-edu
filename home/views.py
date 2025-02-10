from django.shortcuts import render, HttpResponse
from .models import Services
# Create your views here.
def django_home(request):
    sevices = Services.objects.all()

    context = {
        'sevices': sevices,

    }
    return render (request, "home.html", context)



# def django_about(request):
#     return HttpResponse ("about pages")


# def services(request):
#     return HttpResponse ("services pages")

   
