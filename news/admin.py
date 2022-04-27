from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    search_fields = ['date', 'title', 'description']
    list_filter = ['date','title']