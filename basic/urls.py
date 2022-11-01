from django.urls import path 
from .views import *


urlpatterns = [
    path('',index, name='home'),
    # path('search', Search_Results, name='search'),
    path('videoapi/', VideoAPI, name='videoapi'),
    path('<str:urls>', index, name='home')
]