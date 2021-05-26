from django.shortcuts import render

# Create your views here.
def initial_page(request):
    return render(request,'manager/initialpage.html')

def menu_read():
    return None

def menu_update():
    return None