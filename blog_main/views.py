from django.shortcuts import render ,redirect
from blog.models import Category, Blog
from aaboutus.models import About
from .forms import RegistraionForm 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
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

def register(request):
    if request.method=='POST':
        form=RegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form=RegistraionForm()

    context={
        'form':form,

    }
    return render(request, 'register.html',context)



def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
        else:
            print(form.errors)


    form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request, 'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')
# Compare this snippet from blog_main/context_processors.py: