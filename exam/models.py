from django.db import models
from rest_framework import serializers


# Create your models here.


class Exam(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField
    duration = models.IntegerField(default=60)  # exam time in minutes
    date = models.TimeField  # time of exam
    address = models.TextField


class Question(models.Model):
    text = models.CharField(max_length=150)
    score = models.IntegerField(default=1)
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
