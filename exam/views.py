from rest_framework import viewsets, status
# from exam.models import Exams
from exam.models import Exams, Question, Choice, Answer
# from exam.serializers import ExamsSerializer
from exam.serializers import ExamsSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer


class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
