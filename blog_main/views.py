from django.shortcuts import render
from blog.models import Category, Blog
from aaboutus.models import About
def home(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(IS_FEATURED=True,status='Published').order_by('-updated_at')
    post=Blog.objects.filter( IS_FEATURED=False,status='Published')
    # print(post)
    try:
        about=About.objects.get()
    except About.DoesNotExist:
        about=None

    context={
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':post,
        'about':about,
    }
    return render(request, 'home.html', context) 


# def aboutus(request):
#     return render(request, 'aboutus.html')

