from django.db import models
# from user.models import User
from user.models import CustomUser


class Exams(models.Model):
    title = models.CharField(max_length=150, default=None)
    description = models.TextField
    duration = models.IntegerField(default=60)  # exam time in minutes
    date = models.TimeField  # time of exam
    address = models.TextField
    creator = models.ForeignKey(CustomUser, related_query_name='user_id', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=150, default=None)
    score = models.IntegerField(default=1)
    exam = models.ManyToManyField(to=Exams)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    choice_text = models.CharField(max_length=255)

    # votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, default=1)
    exam = models.ForeignKey(to=Exams, on_delete=models.CASCADE)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(to=Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_id.choice_text
