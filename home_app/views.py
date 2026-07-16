from django.shortcuts import render

# Create your views here.
from rezoomeh_site_app.models import *
from rezoomeh_way_app.models import *
from rezoomeh_abzar_app.models import *
from ticket_app.models import *

def home(request):
    Me=AboutMe.objects.first()
    fanavaries=Fanavary.objects.all()
    sits=Site.objects.all()
    abzars=Category.objects.all()
    ways=Way.objects.all()
    context = {
        'Me':Me,
        'fanavaries':fanavaries,
        'sits':sits,
        'abzars':abzars,
        'ways':ways,
    }
    return render(request,'home_app/index.html',context)
