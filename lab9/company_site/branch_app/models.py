from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.name
