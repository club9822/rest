from rest_framework import viewsets, status
# from exam.models import Exams
from exam.models import Exams, Question, Choice, Answer
# from exam.serializers import ExamsSerializer
from exam.serializers import ExamsSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

"""
 viewsets GenericViewSet,ModelViewSet
 mixins ListModelMixin CreateModelMixin

"""


class ExamsViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(exam=self.request.exam)
    #
    # def perform_create(self, serializer):
    #     serializer.save(exam=self.request.exam)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('-id')
    serializer_class = AnswerSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
