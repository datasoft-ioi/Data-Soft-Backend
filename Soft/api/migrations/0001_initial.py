# Generated by Django 4.1.7 on 2023-03-29 12:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('rus_title', models.CharField(max_length=200)),
                ('rus_desc', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/galley/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='HomeTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uz_title', models.CharField(max_length=200)),
                ('ru_title', models.CharField(max_length=200)),
                ('uz_mini_desc', models.CharField(max_length=200)),
                ('ru_mini_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InfoDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('rus_name', models.CharField(max_length=50)),
                ('rus_title', models.CharField(max_length=200)),
                ('rus_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurCoreServis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('rus_name', models.CharField(max_length=50)),
                ('rust_title', models.CharField(max_length=200)),
                ('rus_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/%Y/%m/%d')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
