from django import forms
from blog.models import Category,Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
    



class AddUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','is_staff','is_active','is_superuser','groups','user_permissions']



class EditUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','is_staff','is_active','is_superuser','groups','user_permissions']