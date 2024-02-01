# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post

class PostListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

"""def post_list(request):
    object_list = Post.objects.filter(status="published")
    paginator = Paginator(object_list, 3)  # 3 pasty na staronku
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Kali page nie integer, viartajem pieršuju staronku
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        # Kali page vychodzić za miežy, viartajem apošniuju staronku
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})"""

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,'blog/post/detail.html', {'post': post})
