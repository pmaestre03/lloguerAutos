from django.contrib import admin
from django.urls import path
from lloguer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewAutomobil),
]