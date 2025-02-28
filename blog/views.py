from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from blog.models import Blog,Category , Comment # from .models import Blog will also work
from aaboutus.models import About
from django.db.models import Q
# Create your views here.

def posts_by_category(request,category_id):
    # fetch the posts that belogns to the category with the id category_id
    posts=Blog.objects.filter(status='Published', category=category_id)
    #use try/except when we want to do some custom action if the category does not exists
    # try:
    #     category=Category.objects.get(pk=category_id)
    # except Category.DoesNotExist:
    #     return redirct('home')
    #use ge_object_or_404 when you want to show 404 error page if the category does'nt exist.
    category=get_object_or_404(Category,pk=category_id)
    
    context={
        'posts':posts,
        'category':category,
        
    }
    return  render(request, 'posts_by_category.html', context)

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status='Published')
    # if request.method=='POST':
    #     comment=Comment()
    #     comment.user=request.user
    #     comment.blog=single_blog
    #     comment.comment=request.POST.get('comment')
    #     comment.save()
    #     return redirect(request.path_info)          # below method is better.......

    ########### belows method is better than above method ##########
    if request.method == 'POST' and request.user.is_authenticated:
        comment_text = request.POST.get('comment')              # get the comment from the form it is input textarea name
        if comment_text:
            # Create and save comment directly
            new_comment = Comment(
                user=request.user,
                blog=single_blog,
                comment=comment_text
            )
            new_comment.save()
            # Redirect to avoid form resubmission
            return redirect('blogs', slug=slug)

    comments=Comment.objects.filter(blog=single_blog)
    comments_count=comments.count()
    # print(comments)
    context={
        'single_blog':single_blog,
        'comments':comments,
        'comments_count':comments_count,
    }
    return render(request, 'blogs.html',context)

def search(request):
    keyword=request.GET.get('keyword')

    blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(excerpt__icontains=keyword),status='Published')

    context={
         'keyword':keyword,
         'blogs':blogs,
         

    }
    # blogs=
    return render(request, 'search.html',context)



