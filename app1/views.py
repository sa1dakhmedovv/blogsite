from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import TemplateView

from .forms import CommentForm
from  .models import Post

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list,2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'post_list.html',{'posts':posts})

from .forms import CommentForm

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            print(comments)
        else:
            comment_form = CommentForm()

    return render(request, 'detail_list.html',
                  {'post':post, 'comments':comments, 'new_comment':new_comment})

