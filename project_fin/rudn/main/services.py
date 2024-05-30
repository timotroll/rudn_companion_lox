from . import models
from django.shortcuts import render


def day_to_data(day, group_id, number):
    if day == 'monday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).schedule.monday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).schedule.monday.first
        elif number == 3:
            return models.groups.objects.get(pk=group_id).schedule.monday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).schedule.monday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).schedule.monday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).schedule.monday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).schedule.monday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).schedule.monday.eighth
    elif day == 'tuesday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).schedule.tuesday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).schedule.tuesday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).schedule.tuesday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).schedule.tuesday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).schedule.tuesday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).schedule.tuesday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).schedule.tuesday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).schedule.tuesday.eighth
    elif day == 'wednesday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).schedule.wednesday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).schedule.wednesday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).schedule.wednesday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).schedule.wednesday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).schedule.wednesday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).schedule.wednesday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).schedule.wednesday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).schedule.wednesday.eighth
    elif day == 'thursday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).schedule.thursday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).schedule.thursday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).schedule.thursday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).schedule.thursday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).schedule.thursday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).schedule.thursday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).schedule.thursday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).schedule.thursday.eighth
    elif day == 'friday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).schedule.friday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).schedule.friday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).schedule.friday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).schedule.friday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).schedule.friday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).schedule.friday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).schedule.friday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).schedule.friday.eighth
    elif day == 'saturday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).schedule.saturday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).schedule.saturday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).schedule.saturday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).schedule.saturday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).schedule.saturday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).schedule.saturday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).schedule.saturday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).schedule.saturday.eighth
