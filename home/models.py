from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    images = models.ImageField(upload_to='images')
    

    def __str__(self):
        return self.title
    
