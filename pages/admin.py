from django.contrib import admin
from .models import table1

# Register your models here.

@admin.register(table1)
class AuthorAdmin(admin.ModelAdmin):
    pass