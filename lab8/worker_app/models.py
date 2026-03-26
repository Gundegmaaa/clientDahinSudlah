from django.db import models

from branch_app.models import Branch


class Worker(models.Model):
    wname = models.CharField(max_length=256)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="workers")

    def __str__(self) -> str:
        return self.wname
