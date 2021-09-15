from django.contrib import admin
from . import models

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    list_filter = ['created']
    search_fields = ['name', 'email', 'description']



@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'tel', 'created']
    list_filter = ['created', 'updated']
    search_fields = ['name', 'email', 'description']

