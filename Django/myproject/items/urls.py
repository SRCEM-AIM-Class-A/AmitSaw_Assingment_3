# myproject/urls.py

from django.contrib import admin
from django.urls import path
from items import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('add-item/', views.add_item, name='add_item'),
]
