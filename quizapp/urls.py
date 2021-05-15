from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('final_page/',views.final_page,name='final_page'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
]