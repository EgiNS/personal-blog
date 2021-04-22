from django.shortcuts import render, redirect
from myblog.models import Halaman


def home(request):
    blog1 = Halaman.objects.get(id=4)
    blog2 = Halaman.objects.get(id=5)
    blog3 = Halaman.objects.get(id=6)
    
    konteks = {
        'blog1' : blog1,
        'blog2' : blog2,
        'blog3' : blog3,
    }

    return render(request, 'home.html', konteks)


def tampil_halaman(request):
    tulisan = Halaman.objects.all()

    konteks = {
        'tulisan' : tulisan,
    }

    return render(request, 'blog.html', konteks)


def full_artikel(request, id_halaman):
    artk = Halaman.objects.get(id=id_halaman)

    konteks = {
        'artk' : artk,
    }

    return render(request, 'full-artikel.html', konteks)