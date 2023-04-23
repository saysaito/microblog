from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from blog.forms import CommentForm
from blog.models import Post


def frontpage(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,10)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    return render(request,'blog/frontpage.html',{'posts':posts})
# Create your views here.

def post_detail(request,slug):
    post=Post.objects.get(slug=slug)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',slug=post.slug)
    else:
        form=CommentForm()
    return render(request,'blog/post_detail.html',{'post':post,'form':form})

