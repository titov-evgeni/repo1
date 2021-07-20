from django.db import models
from django.contrib.postgres.fields import JSONField


class InputModel(models.Model):
    field = models.CharField(max_length=30)
    user_input = JSONField()

    def __str__(self):
        return self.field, self.user_input
