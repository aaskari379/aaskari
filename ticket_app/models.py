from django.db import models

# Create your models here.
class Ticket(models.Model):
    name_family = models.CharField(max_length=150)
    mozoo=models.CharField(max_length=100)
    text= models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_family