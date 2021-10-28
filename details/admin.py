from django.contrib import admin
from . import models

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    # disply name -email - subject
    list_display = ['name', 'email', 'subject']
    # filter by created
    list_filter = ['created']
    # search by name - email - description
    search_fields = ['name', 'email', 'description']

@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    # display name - email - tel - created
    list_display = ['name', 'email', 'tel', 'created']
    # filter by created - updated
    list_filter = ['created', 'updated']
    # search by name - email -description
    search_fields = ['name', 'email', 'description']

