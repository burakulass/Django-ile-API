from calendar import c
from multiprocessing import context
from . models import Metro 
#from . models import Hastane
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):

    return render(request, "home.html", )

def Metrolar_list(request):
    metro = Metro.objects.values() # .values ile for döngüsü yaaz ardından filter ile LineNameleri filtrele

    metro_names = []
    for i in metro:
        if i["WC"]: i["WC"] = "Var"
        else: i["WC"] = "Yok"

        if i["BabyRoom"]: i["BabyRoom"] = "Var"
        else: i["BabyRoom"] = "Yok"

        if i["Masjid"]: i["Masjid"] = "Var"
        else: i["Masjid"] = "Yok"

    # metro isimlerini set etmemize yarıyor

        metro_names.append(i["LineName"])
        metro_names =  list(set(metro_names))

    context = {
        'metro': metro,
        "metro_names":metro_names
    }

    return render(request, "Metrolar.html", context )

def Hastaneler_list(request):

    

    context = {
        
    }


    return render(request,"Hastaneler.html", context)