from .models import *
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def initial_page(request):
    date = datetime.today().strftime("%Y-%m-%d")
    profile = Profile.objects.get(user = request.user)
    cafe = profile.Cafeteria.name
    data={
        'date' : date,
        'cafe' : cafe
    }

    return render(request,'manager/initialpage.html', data)

def menu_read(request, date):

    menus = Menu.objects.filter(sale_date = date)
    profile = Profile.objects.get(user = request.user)
    cafe = profile.Cafeteria.name

    data={
        'menus' : menus,
        'cafe' : cafe
    }

    return render(request,'manager/manage_read.html', data)


def menu_update():
    return null