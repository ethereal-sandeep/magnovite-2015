from django.contrib import admin

from .models import Thread, Message

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'is_pending']
    list_filter = ['is_pending']


@admin.register(Message)
class MessaegAdmin(admin.ModelAdmin):
    search_fields = ['thread__id']
    list_display = ['thread', 'timestamp', 'is_staff']
    list_filter = ['is_staff']
