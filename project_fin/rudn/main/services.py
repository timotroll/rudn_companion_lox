from .models import groups, chet, nechet, schedule
from django.shortcuts import render
import sqlalchemy

def GetPareNum(hour, minute):
    hours = ['|', 9, '|', 10, '|', 12, '|', 13, '|', 15, '|', 16, '|', 18, '|', 19, '|']
    if minute <= 20 and hour%3 == 0:
        ind = 0
        for i in hours:
            if hour == i:
                return ind
            else:
                ind += 1
    if minute <= 20 and hour%3 != 0:
        ind = 0
        for i in hours:
            if hour == i:
                return ind-2
            else:
                ind += 1
    if minute > 20:
        ind = 0
        for i in hours:
            if hour == i:
                return ind
            else:
                ind += 1
    

def ChetDayData(day, group_id):
    schedule = [
        groups.objects.get(pk=group_id).schedule.chet.monday,
        groups.objects.get(pk=group_id).schedule.chet.tuesday,
        groups.objects.get(pk=group_id).schedule.chet.wednesday,
        groups.objects.get(pk=group_id).schedule.chet.thursday,
        groups.objects.get(pk=group_id).schedule.chet.friday,
        groups.objects.get(pk=group_id).schedule.chet.saturday
    ]
    CurrentSchedule = schedule[day][4:]
    CurrentSchedule = CurrentSchedule.split('####')
    return CurrentSchedule

def NeChetDayData(day, group_id):
    schedule = [
        groups.objects.get(pk=group_id).schedule.nechet.monday,
        groups.objects.get(pk=group_id).schedule.nechet.tuesday,
        groups.objects.get(pk=group_id).schedule.nechet.wednesday,
        groups.objects.get(pk=group_id).schedule.nechet.thursday,
        groups.objects.get(pk=group_id).schedule.nechet.friday,
        groups.objects.get(pk=group_id).schedule.nechet.saturday
    ]
    CurrentSchedule = schedule[day][4:]
    CurrentSchedule = CurrentSchedule.split('####')
    return CurrentSchedule