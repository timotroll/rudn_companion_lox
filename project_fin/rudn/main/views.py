
from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import CustomUserCreationForm
from .models import News
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

def index(request):
    return render(request, 'main/index.html')


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
from .services import day_to_data

def schedule(request):
    time_dict = ['bag','9:00 - 10:20', '10:30 - 11:50', '12:00 - 13:20', '13:30 - 14:50', '15:00 - 16:20', '16:30 - 17:50', '18:00 - 19:20', '19:30 - 20:50']
    w = models.groups.objects.all()
    if request.POST:
        req = request.POST
        req_dict = dict(req)
        group_id = int(req_dict['group'][0])
        day = req_dict['day'][0]
        group = models.groups.objects.get(pk = group_id).name
        pare = 1
        shedule = []
        while pare <= 8:
            time = time_dict[pare]
            str_object = day_to_data(day, group_id, pare)
            if 2*'|' in str_object:
                name, cat, room = str_object.split('|')
                lesson = {
                    'time': time,
                    'subject': name,
                    'cat': cat,
                    'room': room
                }
                shedule.append(lesson)
            else:
                lesson = {
                    'time': time,
                    'subject': str_object,
                    'room': '',
                    'cat': ''
                }
                shedule.append(lesson)
            pare += 1
        data = {
            'group': group,
            'day': day,
            'schedule': shedule,
            'w': w
        }
        return render(request, 'main/schedule.html', data)
    else:
        if request.user.is_authenticated == True:
            model = get_user_model()
            group_id = request.user.Group.pk
            day_day = datetime.datetime.today().weekday()
            group = models.groups.objects.get(pk = group_id).name
            day_dict = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            day = day_dict[day_day]
            pare = 1
            shedule = []
            while pare <= 8:
                time = time_dict[pare]
                str_object = day_to_data(day, group_id, pare)
                if 2*'|' in str_object:
                    name, cat, room = str_object.split('|')
                    lesson = {
                        'time': time,
                        'subject': name,
                        'cat': cat,
                        'room': room
                    }
                    shedule.append(lesson)
                else:
                    lesson = {
                        'time': time,
                        'subject': str_object,
                        'room': '',
                        'cat': ''
                    }
                    shedule.append(lesson)
                pare += 1
            data = {
                'group': group,
                'day': day,
                'schedule': shedule,
                'w': w
            }
            return render(request, 'main/schedule.html', data)
        else:
            data = {
            'w': w
            }
            return render(request, 'main/schedule.html', data)
    
@login_required
def map(request):
    return render(request, 'main/map.html')

def news(request):
    news_list = News.objects.order_by('-pub_date')
    paginator = Paginator(news_list, 4)  # Показываем 4 новости на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/news.html', {'page_obj': page_obj})