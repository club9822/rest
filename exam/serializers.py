from rest_framework import serializers
# from exam.models import Exams
from exam.models import Exams, Question, Choice,Answer


class ExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exams
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


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
