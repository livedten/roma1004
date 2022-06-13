from django.db import models


# Create your models here.


class MyProject(models.Model):
    field = models.JSONField(blank=True)

    def __str__(self):
        return self.field
