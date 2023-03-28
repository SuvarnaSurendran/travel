from . import views
from django.urls import path


urlpatterns = [

    path('',views.demo,name='demo'),
    path('',views.actor,name='actor'),
    #path('add/',views.addition,name='addition')

]