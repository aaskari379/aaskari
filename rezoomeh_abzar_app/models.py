from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    imoji = models.CharField(max_length=1,blank=True)

    def __str__(self):
        return self.name

class Fanavary(models.Model):
    name = models.CharField(max_length=100)
    fanavaries=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='fanavaries')
    def __str__(self):
        return self.name
