# Generated by Django 2.0 on 2018-10-22 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_readed_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='readed_time',
            new_name='readed_num',
        ),
    ]
