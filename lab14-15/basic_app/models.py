from django.db import models
from django.urls import reverse


class Club(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk': self.pk})


class Comedian(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True, upload_to='static/images')
    club = models.ForeignKey(
        Club, related_name='clubs', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
