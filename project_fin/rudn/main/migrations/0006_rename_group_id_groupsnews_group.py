# Generated by Django 5.0.3 on 2024-07-06 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_categories_news_hashtags_news_cat_groupsnews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groupsnews',
            old_name='group_id',
            new_name='group',
        ),
    ]
