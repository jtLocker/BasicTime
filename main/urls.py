from django.contrib import admin
from django.urls import path
import timeApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', timeApp.views.home, name = "home")
]
