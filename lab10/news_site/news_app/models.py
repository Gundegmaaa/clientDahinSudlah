from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='news')

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self) -> str:
        return self.title
