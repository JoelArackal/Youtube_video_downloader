from django.shortcuts import render, HttpResponse
from pytube import YouTube

# Create your views here.


def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        print(url)
        yt = YouTube(url)
        vids = yt.streams.all()
        print(vids[0])
        y_url = vids[2].url
        return render(request, 'videos.html',{'url': y_url}) 
    # return HttpResponse(f'<h1>Hello {vids[0].title} </h1> <a href="{vids[2].url}">link</a>')
    return render(request, 'index.html')