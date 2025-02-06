from django.contrib import admin

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author','status', 'created_at','IS_FEATURED')
    search_fields = ('id','title', 'category__category_name','status')
    list_editable = ('IS_FEATURED',)
from .models import Category, Blog
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


