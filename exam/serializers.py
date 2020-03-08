from rest_framework import serializers
from exam.models import Exam, Question, Choice


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    # questions = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
