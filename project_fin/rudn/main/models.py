from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now, )

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Group = models.ForeignKey('groups', on_delete=models.SET_NULL, null=True, blank=True)

class groups(models.Model):
    id = models.IntegerField('id',unique=True, primary_key=True)
    name = models.TextField('название группы',max_length=20, unique=True, blank=True)
    slug = models.SlugField('слаг группы',max_length=255, unique=True, db_index=True, blank=True)
    dep_number = models.TextField('номер факультета', max_length=255, blank=True)
    faculty = models.TextField('название факультета', max_length=255, blank=True)
    schedule = models.OneToOneField('schedule', on_delete=models.SET_NULL, null=True, blank=True, related_name='group_shedule')

    def __str__(self):
        return self.name

class schedule(models.Model):
    monday = models.OneToOneField('monday', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='group_monday')
    tuesday = models.OneToOneField('tuesday', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='group_tuesday')
    wednesday = models.OneToOneField('wednesday', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='group_wednesday')
    thursday = models.OneToOneField('thursday', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='group_thursday')
    friday = models.OneToOneField('friday', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='group_friday')
    saturday = models.OneToOneField('saturday', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='group_saturday')


class monday(models.Model):
    id = models.IntegerField('id', unique=True, primary_key=True)
    first = models.TextField('первая пара', max_length=255)
    second = models.TextField('вторая пара', max_length=255)
    third = models.TextField('третья пара', max_length=255)
    forth = models.TextField('четвертая пара', max_length=255)
    fifth = models.TextField('пятая пара', max_length=255)
    sixth = models.TextField('шестая пара', max_length=255)
    seventh = models.TextField('седьмая пара', max_length=255)
    eighth = models.TextField('восьмая пара', max_length=255)

    def __str__(self):
        return self.first

class tuesday(models.Model):
    id = models.IntegerField('id', unique=True, primary_key=True)
    first = models.TextField('первая пара', max_length=255)
    second = models.TextField('вторая пара', max_length=255)
    third = models.TextField('третья пара', max_length=255)
    forth = models.TextField('четвертая пара', max_length=255)
    fifth = models.TextField('пятая пара', max_length=255)
    sixth = models.TextField('шестая пара', max_length=255)
    seventh = models.TextField('седьмая пара', max_length=255)
    eighth = models.TextField('восьмая пара', max_length=255)
    def __str__(self):
        return self.first

class wednesday(models.Model):
    id = models.IntegerField('id', unique=True, primary_key=True)
    first = models.TextField('первая пара', max_length=255)
    second = models.TextField('вторая пара', max_length=255)
    third = models.TextField('третья пара', max_length=255)
    forth = models.TextField('четвертая пара', max_length=255)
    fifth = models.TextField('пятая пара', max_length=255)
    sixth = models.TextField('шестая пара', max_length=255)
    seventh = models.TextField('седьмая пара', max_length=255)
    eighth = models.TextField('восьмая пара', max_length=255)
    def __str__(self):
        return self.first

class thursday(models.Model):
    id = models.IntegerField('id', unique=True, primary_key=True)
    first = models.TextField('первая пара', max_length=255)
    second = models.TextField('вторая пара', max_length=255)
    third = models.TextField('третья пара', max_length=255)
    forth = models.TextField('четвертая пара', max_length=255)
    fifth = models.TextField('пятая пара', max_length=255)
    sixth = models.TextField('шестая пара', max_length=255)
    seventh = models.TextField('седьмая пара', max_length=255)
    eighth = models.TextField('восьмая пара', max_length=255)
    def __str__(self):
        return self.first

class friday(models.Model):
    id = models.IntegerField('id', unique=True, primary_key=True)
    first = models.TextField('первая пара', max_length=255)
    second = models.TextField('вторая пара', max_length=255)
    third = models.TextField('третья пара', max_length=255)
    forth = models.TextField('четвертая пара', max_length=255)
    fifth = models.TextField('пятая пара', max_length=255)
    sixth = models.TextField('шестая пара', max_length=255)
    seventh = models.TextField('седьмая пара', max_length=255)
    eighth = models.TextField('восьмая пара', max_length=255)
    def __str__(self):
        return self.first

class saturday(models.Model):
    id = models.IntegerField('id', unique=True, primary_key=True)
    first = models.TextField('первая пара', max_length=255)
    second = models.TextField('вторая пара', max_length=255)
    third = models.TextField('третья пара', max_length=255)
    forth = models.TextField('четвертая пара', max_length=255)
    fifth = models.TextField('пятая пара', max_length=255)
    sixth = models.TextField('шестая пара', max_length=255)
    seventh = models.TextField('седьмая пара', max_length=255)
    eighth = models.TextField('восьмая пара', max_length=255)

    def __str__(self):
        return self.first