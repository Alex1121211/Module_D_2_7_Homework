# Generated by Django 4.1.6 on 2023-02-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='authorArticle',
        ),
    ]
