from django.shortcuts import render

def initial_page(request):
    return render(request,'manager/initialpage.html')

def menu_read():
    return None

def menu_update():
    return None

def manager_page(request):
    return render(request,'manager/managerPage.html')