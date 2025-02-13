from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    query = request.GET.get('q', '')  
    posts = BlogPost.objects.order_by('-created_at')  

    if query:
        posts = posts.filter(title__icontains=query)  

    paginator = Paginator(posts, 7)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_list.html', {
        'page_obj': page_obj,
        'query': query
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)  

    previous_post = BlogPost.objects.filter(created_at__lt=post.created_at).order_by('-created_at').first()
    next_post = BlogPost.objects.filter(created_at__gt=post.created_at).order_by('created_at').first()

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post
    })
