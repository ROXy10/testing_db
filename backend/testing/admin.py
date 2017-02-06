from django.contrib import admin
from .models import Testing, Test, Question, Answer


class TestAdmin(admin.ModelAdmin):
    list_display = ['test_title', 'is_active']
    list_display_links = ['test_title']
    list_editable = ['is_active']
    ordering = ['test_title']
    list_filter = ['test_title', 'is_active']

    list_per_page = 10
    search_fields = ['test_title']


admin.site.register(Testing)
admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Answer)
