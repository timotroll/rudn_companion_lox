from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
    cat = models.ForeignKey('categories', on_delete=models.SET_NULL, null=True)
    hashtags = models.TextField('хештеги', max_length=255, blank=True)

    def __str__(self):
        return self.title
    
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Group = models.ForeignKey('groups', on_delete=models.SET_NULL, null=True, blank=True)
    is_starosta = models.BooleanField('староста', default=False)
    status = models.TextField('cтатус', max_length=100, default=None, blank=True, null=True)

class groupsnews(models.Model):
    group = models.ForeignKey('groups', on_delete=models.SET_NULL, null=True)
    cat = models.ForeignKey('categories', on_delete=models.SET_NULL, null=True)
    hashtags = models.TextField('хештеги', max_length=255, blank=True)
    body = models.TextField('содержание')
    header = models.CharField('заголовок', max_length=100)
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)

class categories(models.Model):
    category = models.CharField('категория', max_length=25)
    
    def __str__(self):
        return self.category

class groups(models.Model):
    id = models.IntegerField('id',unique=True, primary_key=True)
    name = models.TextField('название группы',max_length=20, unique=True, blank=True)
    slug = models.SlugField('слаг группы',max_length=255, unique=True, db_index=True, blank=True)
    dep_number = models.TextField('номер факультета', max_length=255, blank=True)
    faculty = models.TextField('название факультета', max_length=255, blank=True)
    schedule = models.OneToOneField('schedule', on_delete=models.SET_NULL, null=True, blank=True, default=None, related_name='group_shedule')

    def __str__(self):
        return self.name

class schedule(models.Model):
    chet = models.OneToOneField('chet', on_delete=models.SET_NULL, null=True, blank=True, related_name='chet_shedule')
    nechet = models.OneToOneField('nechet', on_delete=models.SET_NULL, null=True, blank=True, related_name='nechet_shedule')

class chet(models.Model):
    monday = models.TextField('понедельник', max_length=255, blank=True)
    tuesday = models.TextField('вторник', max_length=255, blank=True)
    wednesday = models.TextField('среда', max_length=255, blank=True)
    thursday = models.TextField('четверг', max_length=255, blank=True)
    friday = models.TextField('пятница', max_length=255, blank=True)
    saturday = models.TextField('суббота', max_length=255, blank=True)

class nechet(models.Model):
    monday = models.TextField('понедельник', max_length=255, blank=True)
    tuesday = models.TextField('вторник', max_length=255, blank=True)
    wednesday = models.TextField('среда', max_length=255, blank=True)
    thursday = models.TextField('четверг', max_length=255, blank=True)
    friday = models.TextField('пятница', max_length=255, blank=True)
    saturday = models.TextField('суббота', max_length=255, blank=True)

class schedulechange(models.Model):
    dbrequest = models.TextField('запрос', max_length=255)
    execution = models.TextField('изменение', max_length=255)