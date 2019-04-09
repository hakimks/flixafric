from django.db import models
from django.contrib.auth.model import User

from django.utils import timezone

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    poster = models.ImageField(upload_to="posters" default="poster/default.jpg")
    mainbackdrop = models.ImageField(upload_to="backdrop")
    otherbackdrop = models.ImageField(upload_to="backdrop")
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date =  models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=150)
    genre = models.ForeignKey(Genre, on_delete=modes.CASCADE)
    actors = models.ManyToManyField(Actor, through='MovieActor')
    productioncompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    length = models.IntergerField()

    def __str__(self):
        return self.title

    def Meta:
        ordering = ["created_date"]

class Actor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photos/actor" default="photos/actot/default.jpg")

    def __str__(sef):
        return self.names

class Genre(models.Model):
    """ Holds the Genres like Action, Thriller """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Director(models.Model):
    """ Holds the Name of the movie Director """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Company(models.Model):
    """ Holds the Name of the production Company """
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="photos/productco" default="photos/productco/default.jpg")

    def __str__(self):
        return self.name