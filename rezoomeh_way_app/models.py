from django.db import models

# Create your models here.
class Way(models.Model):
    title = models.CharField(max_length=100)
    bazeh_zamani = models.CharField(max_length=150)
    description = models.TextField()
    mesal=models.TextField()
    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile = models.ImageField(upload_to='profile/')
    maharat=models.CharField(max_length=100)
    def __str__(self):
        return self.name


