from django.db import models

class Branch(models.Model):
    bname = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.bname
