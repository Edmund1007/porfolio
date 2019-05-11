from django.shortcuts import render
from gallery.models import Gallery


def home(requset):
    gallerys = Gallery.objects
    return render(requset, 'home.html', {'gallerys': gallerys})


    