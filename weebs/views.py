from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post, ManhwaPost

def index(request):
    sliderposts = Post.objects.all()
    manhwapost = ManhwaPost.objects.all()
    return render(request,'weebs/index.html',{
        "sliderposts":sliderposts,
        "manhwapost":manhwapost,
    })


def article_detail(request,pk ):
    post = Post.objects.filter(pk=pk)
    manhwapost = ManhwaPost.objects.filter(pk=pk)
    return render(request,'weebs/article-detail.html',{
        "post":post,
        "manhwapost":manhwapost,
    })


def category(request):
    return render(request,'weebs/category.html')


def manhwa(request):
    return render(request,'weebs/manhwa.html')


def manhua(request):
    return render(request,'weebs/manhua.html')




def about(request):
    return render(request,'weebs/about.html')



def contact(request):
    return render(request,'weebs/contact.html')
