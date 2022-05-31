from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request,'weebs/index.html',{
        "posts":posts,
    })


def article_detail(request,pk ):
    post = Post.objects.filter(pk=pk)
    return render(request,'weebs/article-detail.html',{
        "post":post,
    })

def category(request):
    return render(request,'weebs/category.html')

def anime(request):
    return render(request,'weebs/anime.html')


def manhwa(request):
    return render(request,'weebs/manhwa.html')


def manhua(request):
    return render(request,'weebs/manhua.html')


def doujins(request):
    return render(request,'weebs/doujins.html')


def hentai(request):
    return render(request,'weebs/hentai.html')

def about(request):
    return render(request,'weebs/about.html')

def single_audio(request):
    return render(request,'weebs/single-audio.html')

def single_gallery(request):
    return render(request,'weebs/single-gallery.html')

def single_standard(request):
    return render(request,'weebs/single-standard.html')

def single_video(request):
    return render(request,'weebs/single-video.html')

def contact(request):
    return render(request,'weebs/contact.html')
