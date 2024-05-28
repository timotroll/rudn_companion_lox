from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule'),
    path('map/', views.map, name='map'),
    path('news/', views.news, name='news'),
]


