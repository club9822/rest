from django.db import models
from user.models import User


# Create your models here.
class SampleModel(models.model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FilePathField()
    creator = models.ForeignKey(to=User, related_name='sampleapp', on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.title)
