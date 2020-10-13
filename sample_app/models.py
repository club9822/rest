from django.db import models
from user.models import CustomUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class SampleModel(models.model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FilePathField()
    creator = models.ForeignKey(to=CustomUser, related_name='sampleapp', on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.title)
