from django.shortcuts import render

from blog.models import Post


def frontpage(request):
    posts=Post.objects.all()
    return render(request,'blog/frontpage.html',{'posts':posts})
# Create your views here.

