from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, groupsnews, News

admin.site.register(User, UserAdmin)
admin.site.register(News)
admin.site.register(groupsnews)
