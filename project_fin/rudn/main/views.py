
from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, get_user_model
from .models import News
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from taggit.models import TaggedItem, Tag


def index(request):
    return render(request, 'main/index.html')


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
from .services import ChetDayData, NeChetDayData, GetPareNum

def schedule(request):
    time_dict = ['bag','9:00 - 10:20', '10:30 - 11:50', '12:00 - 13:20', '13:30 - 14:50', '15:00 - 16:20', '16:30 - 17:50', '18:00 - 19:20', '19:30 - 20:50', '21:00 - 22:20']
    day_dict = ['bag', 'Понедельник', 'Вторник', 'Среду', 'Четверг', 'Пятницу', 'Субботу']
    w = models.groups.objects.all()
    if request.POST:
        req = request.POST
        req_dict = dict(req)
        group_id = int(req_dict['group'][0])
        day = int(req_dict['day'][0])
        week = int(req_dict['week'][0])
        group = models.groups.objects.get(pk = group_id).name
        if week == 1:
            CurrentSchedule = ChetDayData(day - 1, group_id)
        else:
            CurrentSchedule = NeChetDayData(day - 1 , group_id)
        shedule = []
        pare = 0
        for ind in CurrentSchedule:
            pare += 1
            time = time_dict[pare]
            if 2*'|' in ind:
                name, cat, room = ind.split('|')
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
                    'subject': ind,
                    'room': '',
                    'cat': ''
                }
                shedule.append(lesson)
        data = {
            'group_val': group_id,
            'group': group,
            'day': day_dict[day],
            'schedule': shedule,
            'w': w
        }
        return render(request, 'main/schedule.html', data)
    else:
        if request.user.is_authenticated == True:
            model = get_user_model()
            group_id = request.user.Group.pk
            is_starosta = request.user.is_starosta
            day_day = datetime.datetime.today().weekday()
            cur_hour = datetime.datetime.now().hour
            cur_min = datetime.datetime.now().minute
            pare_num = str(GetPareNum(cur_hour, cur_min))
            week = datetime.date.today().isocalendar().weekday
            group = models.groups.objects.get(pk = group_id).name
            day = day_dict[day_day]
            pare = 0
            if week % 2 == 0:
                CurrentSchedule = ChetDayData(day_day - 1, group_id)
            else:
                CurrentSchedule = NeChetDayData(day_day - 1, group_id)
            shedule = []
            for ind in CurrentSchedule:
                pare += 1
                time = time_dict[pare]
                if 2*'|' in ind:
                    name, cat, room = ind.split('|')
                    lesson = {
                        'time': time,
                        'subject': name,
                        'cat': cat,
                        'room': room,
                        'is_starosta': is_starosta
                    }
                    shedule.append(lesson)
                else:
                    lesson = {
                        'time': time,
                        'subject': ind,
                        'room': '',
                        'cat': '',
                        'is_starosta': is_starosta
                    }
                    shedule.append(lesson)
            data = {
                'group_val': group_id,
                'group': group,
                'day': day_dict[day_day],
                'schedule': shedule,
                'w': w,
                'is_starosta': is_starosta,
                'pare_num': pare_num
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
    AllImagaes = models.newsimages.objects.all()
    for img in AllImagaes:
        string = str(img.image)
        if string[0] == 'm':
            img.image = string[12:]
            img.save()
            
    AllTags = Tag.objects.all()
    news_list = News.objects.order_by('-pub_date')
    paginator = Paginator(news_list, 4)  # Показываем 4 новости на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/news.html', {'page_obj': page_obj, 'AllTags': AllTags, 'AllImages': AllImagaes})

def ShowTagNewsList(request, tag_slug):
    AllTags = Tag.objects.all()
    # news_list = models.News.objects.filter(title__contains=(TaggedItem.objects.all().filter(tag = Tag.objects.get(slug = tag_slug)).filter(content_type = 4)))
    news_list = models.News.objects.filter(tags__name__in=[tag_slug]).order_by('-pub_date')
    paginator = Paginator(news_list, 4)  # Показываем 4 новости на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/news.html', {'page_obj': page_obj,  'AllTags': AllTags})

def ScheduleChange(request):
    if request.POST:
        req = request.POST
        req_dict = dict(req)
        chetnost = req_dict['chetnost'][0]
        day = req_dict['day'][0]
        para_num = req_dict['num'][0]
        group_id = request.user.Group.id
        para_name = req_dict['para'][0]
        cat_para = req_dict['cat'][0]
        class_num = req_dict['class'][0]
        new_req = para_name + '|' + cat_para + '|' + class_num
        db_exec_day = 'groups.objects.get(pk = ' + str(group_id) + ').schedule.' + chetnost + '.' + day
        changes = str(para_num) + '####' + new_req
        models.schedulechange.objects.create(dbrequest = db_exec_day, execution = changes)
        DayToChange = eval('models.' + db_exec_day)[4:]
        DaytoChangeDict = DayToChange.split('####')
        flag = 0
        NewDayChanged = ''
        for ind in DaytoChangeDict: 
            flag += 1
            if flag == int(para_num):
                Pare = new_req
                NewDayChanged = NewDayChanged + '####' + str(Pare)
            else:
                NewDayChanged = NewDayChanged + '####' + str(ind)
        print(NewDayChanged)
        db_exec = f'models.{chetnost}.objects.filter(pk = {group_id}).update({day} = "{NewDayChanged}")'
        eval(db_exec)


    if request.user.is_authenticated == True:
        if request.user.is_starosta == 1:
            return render(request, 'main/ScheduleChange.html')
    else:
        return HttpResponse('Доступно только старостам')

def GroupNews(request):
    if request.user.is_authenticated == True:
        group_id = request.user.Group.id
        News = models.groupsnews.objects.filter(group = group_id).order_by('-pub_date')
        paginator = Paginator(News, 4)  # Показываем 4 новости на странице

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'news':News,
            'page_obj':page_obj
        }
        return render(request, 'main/GroupNews.html', data)
    else:
        return HttpResponseRedirect(reverse('users:login'))
    
def GroupNewsCreate(request):
    if request.POST:
        req = request.POST
        req_dict = dict(req)
        group_id = request.user.Group.id
        body = req_dict['body'][0] 
        header = req_dict['header'][0]
        pub_date = datetime.date.today()
        cats = models.categories.objects.get(pk = int(req_dict['cat'][0]))
        hashtags = req_dict['hash'][0]
        models.groupsnews.objects.create(hashtags=hashtags, body=body, header=header, pub_date=pub_date, cat=cats, group_id=group_id)
    if request.user.is_authenticated == True:
        if request.user.is_starosta == 1:
            categories = models.categories.objects.all()
            data = {
                'categories':categories
            }
            return render(request, 'main/GroupNewsCreate.html', data)
        else:
            return HttpResponse('тока для старост')
    else:
        return HttpResponseRedirect(reverse('user:login'))

def UserNotes(request):
    if request.user.is_authenticated == True:
        notes = models.notes.objects.filter( user = request.user.pk ).order_by('-date')
        data = {
            'notes':notes,
        }
        return render(request, 'main/UserNotes.html')
    else:
        return HttpResponseRedirect(reverse('user:login'))
    
