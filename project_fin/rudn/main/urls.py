from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule'),
    path('map/', views.map, name='map'),
    path('news/', views.news, name='news'),
    path('schedule/change', views.ScheduleChange, name='ScheduleChange'),
    path('news/group/', views.GroupNews, name='GroupNews'),
    path('news/group/create/', views.GroupNewsCreate, name='GroupNewsCreate'),
    path('notes/', views.UserNotes, name='UserNotes'),
    path('news/tag/<str:tag_slug>/', views.ShowTagNewsList, name='TagNews')
]


