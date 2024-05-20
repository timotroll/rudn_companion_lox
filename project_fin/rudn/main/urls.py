from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule'),
    path('map/', views.map, name='map'),
    path('news/', views.news, name='news'),
    path('register/', views.register, name='register'),
    path('log/', views.CustomLoginView.as_view(), name='log'),
]


