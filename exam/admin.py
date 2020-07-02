from django.contrib import admin
from exam.models import Exams
# from exam.models import Exam, Question, Choice


# Register your models here.

class ExamsAdmin(admin.ModelAdmin):
    pass


# class QuestionAdmin(admin.ModelAdmin):
#     pass
#
#
# class ChoiceAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Exams, ExamsAdmin)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
