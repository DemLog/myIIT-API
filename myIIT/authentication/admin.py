from django.contrib import admin
from .models import User


@admin.register(User)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['email', 'get_full_name', 'study_group']
