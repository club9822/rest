from django.contrib import admin
from exam.models import Exam, Question, Choice


# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class ChoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
