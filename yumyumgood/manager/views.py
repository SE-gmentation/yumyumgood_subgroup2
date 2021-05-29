from .models import *
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def initial_page(request):
    date = datetime.today().strftime("%Y-%m-%d")
    data={
        'date' : date
    }

    return render(request,'manager/initialpage.html', data)

def menu_read(request, date):

    menus = Menu.objects.filter(sale_date = date)
    data={
        'menus' : menus
    }
    print(date)
    return render(request,'manager/manage_read.html', data)


def menu_update():
    return null