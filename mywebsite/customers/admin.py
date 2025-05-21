from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Books

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'title', 'author', 'price', 'created_on')

