from django.shortcuts import get_object_or_404, render,redirect
from blog.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
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
