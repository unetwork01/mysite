# Generated by Django 2.0 on 2018-10-22 01:33

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181020_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
