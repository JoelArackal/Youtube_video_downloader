from django.shortcuts import render, HttpResponse
from pytube import YouTube

# Create your views here.


def index(request):
    url = 'https://www.youtube.com/watch?v=c45fVxBnUFs'
    yt = YouTube(url)
    vids = yt.streams.all()
    print(vids[0])
    return HttpResponse(f'<h1>Hello {vids[0].title} </h1> <a href="{vids[2].url}">link</a>')