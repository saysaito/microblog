from django.shortcuts import render
def frontpage(request):
    return render(request,'blog/frontpage.html')
# Create your views here.
