from django.shortcuts import get_object_or_404, render,redirect
from blog.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm ,BlogPostForm
from django.template.defaultfilters import slugify

# Compare this snippet from dashboardx/views.py:

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    Blog_count=Blog.objects.all().count()
    context={   
        'category_count':category_count,
        'Blog_count':Blog_count,
    }

    return render(request, 'dashboardx/dashboard.html',context)

def category(request):
    categories=Category.objects.all()
    context={
        'categories':categories,
    }
    return render(request, 'dashboardx/category.html',context)

def add_category(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')

    form=CategoryForm()

    context={
        'form':form,
    }
    return render(request, 'dashboardx/add_category.html',context)


def edit_category(request,id):
    category=get_object_or_404(Category,pk=id)
    
    if request.method=='POST':
        form=CategoryForm(request.POST ,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    form=CategoryForm(instance=category)
    context={
        'form':form,
        'category':category,

    }
    return render(request, 'dashboardx/edit_category.html',context)





def delete_category(request,id):
    category=get_object_or_404(Category,pk=id)
    category.delete()
    return redirect('category')
    #



# from here on post crud

def posts(request):
    posts=Blog.objects.all()
    context={
        'posts':posts,
    }
    return render(request, 'dashboardx/posts.html',context)



# def add_post(request):
    
#     if request.method=='POST':
#         form=BlogPostForm(request.POST ,request.FILES)
#         print(form)
#         if form.is_valid():
#             post=form.save(commit=False)  #  temporary save
#             post.author=request.user
#             post.save()    # form is saved permanently .   it is saved earlier to get its id save so we can use it further to genrate unique id.
#             title=form.cleaned_data.get('title')
#             post.slug=slugify(title)   +  '-' + str(post.id)
           
#             post.save()
           
#             return redirect('posts')
#         else:
#             print('form is invalid')
#             print(form.errors)   
#     form=BlogPostForm()
#     context={
#         'form':form,
#     }

#     return render(request, 'dashboardx/add_post.html',context)


def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporarily saving the form
            post.author = request.user
            post.save()   # need to save so that unique id is generated in next few line of code.
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboardx/add_post.html', context)




def edit_post(request,id):
    post=get_object_or_404(Blog,pk=id)
    if request.method=='POST':
        form=BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            title=form.cleaned_data.get('title')
            post.slug=slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    form=BlogPostForm(instance=post)
    context={
    'form':form,
     'post':post,
    }


    return render(request, 'dashboardx/edit_post.html',context)


def delete_post(request,id):
    post=get_object_or_404(Blog,pk=id)
    post.delete()
    return redirect('posts')