from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.


class ArtWork(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='assets/')
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
