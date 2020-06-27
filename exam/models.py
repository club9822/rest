from django.db import models
from user.models import User


class Exam(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField
    duration = models.IntegerField(default=60)  # exam time in minutes
    date = models.TimeField  # time of exam
    address = models.TextField
    creator = models.ForeignKey(to=User, related_name='exams', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=150)
    score = models.IntegerField(default=1)
    exam = models.ManyToManyField(to=Exam)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, default=1)
    choice_text = models.CharField(max_length=200)

    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class Answer(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    question_id = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(to=Choice, on_delete=models.CASCADE)
