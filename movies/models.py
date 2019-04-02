from django.db import models
from django.contrib.auth.model import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    poster = models.ImageField(upload_to="posters" default="poster/default.jpg")
    mainbackdrop = models.ImageField(upload_to="backdrop")
    otherbackdrop = models.ImageField(upload_to="backdrop")
    director = models.CharField(max_length=150)
    created_by = models.ForeignKey(User)
    created_date =  models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.title

    def Meta:
        ordering = ["created_date"]
