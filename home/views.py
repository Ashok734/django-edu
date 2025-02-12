from django.shortcuts import render
from .models import Service
# Create your views here.
def home_page(request):

    ashok = Service.objects.all()

    context = {
        'ashok': ashok,

    }

    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html")
    