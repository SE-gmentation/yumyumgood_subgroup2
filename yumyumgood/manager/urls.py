from django.conf.urls import url
from django.urls import path, register_converter
from .views import *
import datetime

app_name = 'manager'

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path("", initial_page, name="initial_page"),
    url(r'^(?P<date>\d{4}-\d{2}-\d{2})/$', menu_read, name='menu_read'),
    url(r'^edit/(?P<date>\d{4}-\d{2}-\d{2})/$', menu_edit, name='menu_edit'),
    url(r'^update/(?P<date>\d{4}-\d{2}-\d{2})/$', menu_update, name='menu_update'),
]
