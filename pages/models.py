from pyexpat import model
from django.db import models

# Create your models here.


class ArtWork(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='assets/')
    featured = models.BooleanField(default=False)
