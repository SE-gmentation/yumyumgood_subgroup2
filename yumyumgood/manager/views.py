from manager.models import *
from django.shortcuts import render

# Create your views here.
def initial_page(request):
    return render(request,'manager/initialpage.html')

def menu_read(request, date):
    test = Menu.objects.all
    # menus = Menu.objects.filter(sale_date = date)
    menu = Menu.objects.get(id = 1)
    data={
        'test' : menu,
        # 'menus': menus
    }

    print(date)
    print(test)
    return render(request,'manager/manage_read.html',data)


def menu_update():
    return null