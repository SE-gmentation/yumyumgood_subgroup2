from .models import *
from django.shortcuts import render, redirect
from datetime import datetime

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
    dates = date.split("-")
    year = dates[0]
    month = dates[1]
    day = dates[2]

    data={
        'menus' : menus,
        'cafe' : cafe,
        'year' : year,
        'month' : month,
        'day' : day,
        'nowdate' : date,
    }

    return render(request,'manager/manage_read.html', data)


def menu_edit(request, date) :
    menus = Menu.objects.filter(sale_date = date)
    profile = Profile.objects.get(user = request.user)

    cafe = profile.Cafeteria.name
    dates = date.split("-")
    year = dates[0]
    month = dates[1]
    day = dates[2]

    data={
        'menus' : menus,
        'cafe' : cafe,
        'year' : year,
        'month' : month,
        'day' : day,
        'nowdate' : date,
    }

    return render(request,'manager/manage_update.html', data)


def menu_update(request, date):

    profile = Profile.objects.get(user = request.user)
    menus = Menu.objects.filter(sale_date = date, cafeteria = profile.Cafeteria)
    allmenu = Menu.objects.all()
    cafe = profile.Cafeteria.name
    dates = date.split("-")
    year = dates[0]
    month = dates[1]
    day = dates[2]
    for i in range(1, allmenu.count()+1) :
        changeMenu = Menu.objects.get(id = i)
        saleDate = str(changeMenu.sale_date)
        if (saleDate == str(date) and changeMenu.cafeteria == profile.Cafeteria) :
            status=request.POST.get('status['+str(i)+']')
            quantity=request.POST.get('quantity['+str(i)+']')
            #DB에 바꿀 내용들
            changeMenu.status=status
            changeMenu.quantity=quantity
            changeMenu.save()

    data={
            'menus' : menus,
            'cafe' : cafe,
            'year' : year,
            'month' : month,
            'day' : day,
            'nowdate' : date,
        }

    return redirect(f'/{date}/')
