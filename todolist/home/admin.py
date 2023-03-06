from django.contrib import admin
from home.models import Task
from django.utils.html import format_html

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskTitle','taskDesc', 'taskUrl', 'click_me')

    def click_me(self, obj):
        return format_html(f'<a href="/admin/home/task/{obj.id}/change/" class="default">view</a>')


admin.site.register(Task, TaskAdmin)


