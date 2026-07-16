from django.db import models

from rezoomeh_abzar_app.models import Fanavary


# Create your models here.
class Site(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    fanavaries = models.ManyToManyField(Fanavary,related_name='sits')
    image = models.ImageField(upload_to='images/')
    demo_url= models.URLField(blank=True)
    github_url= models.URLField(blank=True)
    def __str__(self):
        return self.title
    def __str__(self):
        return self.title
    def __str__(self):
        return self.title