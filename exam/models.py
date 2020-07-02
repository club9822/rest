from django.db import models
# from user.models import User
from django.contrib.auth.models import User


class Exams(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField
    duration = models.IntegerField(default=60)  # exam time in minutes
    date = models.TimeField  # time of exam
    address = models.TextField
    creator = models.ForeignKey(User, related_query_name='user_id', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=150)
    score = models.IntegerField(default=1)
    exam = models.ManyToManyField(to=Exams)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    choice_text = models.CharField(max_length=200)

    # votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    exam = models.ForeignKey(to=Exams, on_delete=models.CASCADE)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(to=Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_id.choice_text
