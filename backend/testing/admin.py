from django.contrib import admin

from .models import Testing, Test, Question, Answer


class QuestionInline(admin.TabularInline):
    model = Question
    show_change_link = True


class TestAdmin(admin.ModelAdmin):
    list_display = ['test_title', 'is_active']
    list_display_links = ['test_title']
    list_editable = ['is_active']
    ordering = ['test_title']
    list_filter = ['test_title', 'is_active']

    list_per_page = 10
    search_fields = ['test_title']

    inlines = [
        QuestionInline,
    ]


class AnswerInline(admin.TabularInline):
    model = Answer
    show_change_link = True


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_title', 'test', 'multi']
    list_display_links = ['question_title']
    list_editable = ['test', 'multi']
    ordering = ['test', 'question_title']
    list_filter = ['test', 'multi']

    list_per_page = 10
    search_fields = ['question_title']

    inlines = [
        AnswerInline,
    ]


class TestingAdmin(admin.ModelAdmin):
    list_display = ['date', 'test', 'user', 'result']
    list_display_links = ['date', 'test', 'user', 'result']
    ordering = ['date', 'test', 'user', 'result']
    list_filter = ['date', 'test', 'user', 'result']

    list_per_page = 10
    search_fields = ['test', 'user']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_title', 'test', 'correct']
    list_display_links = ['answer_title']
    list_editable = ['test', 'correct']
    ordering = ['answer_title', 'test', 'correct']
    list_filter = ['answer_title', 'test', 'correct']

    list_per_page = 10
    search_fields = ['answer_title', 'test']


# date_hierarchy = 'date'

admin.site.register(Testing, TestingAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
