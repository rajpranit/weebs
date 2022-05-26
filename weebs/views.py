from django.shortcuts import render

def index(request):
    return render(request,'weebs/index.html')


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
