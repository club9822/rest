from django.db import models
from user.models import User


class Exam(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField
    duration = models.IntegerField(default=60)  # exam time in minutes
    date = models.TimeField  # time of exam
    address = models.TextField
    creator = models.ForeignKey(to=User, related_name='exams', on_delete=models.CASCADE, default=1)


class Question(models.Model):
    text = models.CharField(max_length=150)
    score = models.IntegerField(default=1)
    exam = models.ForeignKey(to=Exam, related_name='questions', related_query_name='exam', on_delete=models.CASCADE,
                             default=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, default=1)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
