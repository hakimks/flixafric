# Generated by Django 2.1.7 on 2019-04-10 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/actor')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to='photos/company')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to='photos/directors')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('synopsis', models.TextField()),
                ('poster', models.ImageField(upload_to='movies/posters')),
                ('mainbackdrop', models.ImageField(upload_to='backdrop')),
                ('otherbackdrop', models.ImageField(upload_to='backdrop')),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(max_length=150)),
                ('length', models.IntegerField()),
                ('actors', models.ManyToManyField(to='movies.Actor')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Genre')),
                ('productioncompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Company')),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]