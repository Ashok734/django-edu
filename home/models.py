from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=150)
    descriptions = models.TextField()

    def __str__(self):
        return self.title
    
