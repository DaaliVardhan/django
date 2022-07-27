from django.db import models

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    def __str__(self) -> str:
        return self.title