from django.db import models

# Create your models here.
class Friend(models.Model):
    friend = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.friend
