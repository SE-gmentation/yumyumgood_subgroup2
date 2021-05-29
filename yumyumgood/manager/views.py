from .models import *
from django.shortcuts import render

def initial_page(request):
    return render(request,'manager/initialpage.html')

def menu_read(request, date):

    menus = Menu.objects.filter(sale_date = date)
    data={
        'menus' : menus
    }
    print(menus)
    return render(request,'manager/manage_read.html', data)


def menu_update():
    return None

def manager_page(request):
    return render(request, 'manager/managerPage.html')