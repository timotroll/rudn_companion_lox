from . import models


def day_to_data(day, group_id, number):
    if day == 'monday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).shedule.monday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).shedule.monday.first
        elif number == 3:
            return models.groups.objects.get(pk=group_id).shedule.monday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).shedule.monday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).shedule.monday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).shedule.monday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).shedule.monday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).shedule.monday.eighth
    elif day == 'tuesday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).shedule.tuesday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).shedule.tuesday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).shedule.tuesday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).shedule.tuesday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).shedule.tuesday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).shedule.tuesday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).shedule.tuesday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).shedule.tuesday.eighth
    elif day == 'wednesday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).shedule.wednesday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).shedule.wednesday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).shedule.wednesday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).shedule.wednesday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).shedule.wednesday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).shedule.wednesday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).shedule.wednesday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).shedule.wednesday.eighth
    elif day == 'thursday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).shedule.thursday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).shedule.thursday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).shedule.thursday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).shedule.thursday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).shedule.thursday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).shedule.thursday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).shedule.thursday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).shedule.thursday.eighth
    elif day == 'friday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).shedule.friday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).shedule.friday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).shedule.friday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).shedule.friday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).shedule.friday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).shedule.friday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).shedule.friday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).shedule.friday.eighth
    elif day == 'saturday':
        if number == 1:
            return models.groups.objects.get(pk=group_id).shedule.saturday.first
        elif number == 2:
            return models.groups.objects.get(pk=group_id).shedule.saturday.second
        elif number == 3:
            return models.groups.objects.get(pk=group_id).shedule.saturday.third
        elif number == 4:
            return models.groups.objects.get(pk=group_id).shedule.saturday.forth
        elif number == 5:
            return models.groups.objects.get(pk=group_id).shedule.saturday.fifth
        elif number == 6:
            return models.groups.objects.get(pk=group_id).shedule.saturday.sixth
        elif number == 7:
            return models.groups.objects.get(pk=group_id).shedule.saturday.seventh
        elif number == 8:
            return models.groups.objects.get(pk=group_id).shedule.saturday.eighth
