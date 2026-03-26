from django.db import models
from branch_app.models import Branch


class Worker(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='workers')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=120)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    hired_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
