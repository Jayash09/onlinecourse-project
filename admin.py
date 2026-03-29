from django.contrib import admin
from .models import Question, Choice, Submission

# Inline for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Question
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Admin for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Admin for Lesson (dummy if not created)
class LessonAdmin(admin.ModelAdmin):
    pass

# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)