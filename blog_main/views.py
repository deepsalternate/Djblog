from django.shortcuts import render
from blog.models import Category, Blog
def home(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(IS_FEATURED=True,status='Published').order_by('-updated_at')
    post=Blog.objects.filter( IS_FEATURED=False,status='Published')
    # print(post)
    
    context={
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':post
    }
    return render(request, 'home.html', context) 
