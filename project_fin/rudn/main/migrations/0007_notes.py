# Generated by Django 5.0.3 on 2024-07-07 18:27

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_group_id_groupsnews_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=255, verbose_name='заметка')),
                ('header', models.CharField(max_length=20, verbose_name='название')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
