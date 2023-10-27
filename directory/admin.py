from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import TypeTask,Subject


@admin.register(TypeTask)
@admin.register(Subject)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['title']

