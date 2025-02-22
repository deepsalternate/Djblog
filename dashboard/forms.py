from django import forms
from blog.models import Category,Blog

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model=Category
        fields='__all__'
# Compare this snippet from blog/views.py:
# from django.shortcuts import render
# from blog.models import Category, Blog    



class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','category','featured_image','excerpt','content','status','IS_FEATURED']
    



    