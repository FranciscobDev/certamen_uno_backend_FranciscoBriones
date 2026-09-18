from django.urls import path
from . import views

app_name = "app1"

urlpatterns = [
    path('', views.index,name='index'),
    path('vista2/', views.vista2,name='vista2'),

]