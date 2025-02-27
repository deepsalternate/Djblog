from django.urls import path
from .import views



urlpatterns = [
      path('',views.dashboard,name='dashboard'),
      path('category/',views.category,name='category'),
      path('category/add/',views.add_category,name='add_category'),
      path('category/edit/<int:id>/',views.edit_category,name='edit_category'),
      path('category/delete/<int:id>/',views.delete_category,name='delete_category'),
      # blog post crud
      path('posts/',views.posts,name='posts'),
      path('post/add/',views.add_post,name='add_post'), 
      path('post/edit/<int:id>/',views.edit_post,name='edit_post'),
      path('post/delete/<int:id>/',views.delete_post,name='delete_post'),
      # user crud

      path('users/',views.users,name='users'),
      path('users/add/',views.add_user,name='add_user'),
      path('users/edit/<int:id>/',views.edit_user,name='edit_user'),
      path('users/delete/<int:id>/',views.delete_user,name='delete_user'),
]