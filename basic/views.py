from django.shortcuts import render, HttpResponse
from pytube import YouTube, Search

# Create your views here.


def index(request):
    if request.GET.get('url', None):
        url = request.GET['url']
        print(url)
        yt = YouTube(url)
        vids = yt.streams.all()
        print(vids[0])
        y_url = vids[2].url
        return render(request, 'videos.html',{'url': y_url}) 
    # return HttpResponse(f'<h1>Hello {vids[0].title} </h1> <a href="{vids[2].url}">link</a>')
    return render(request, 'index.html')


def Search_Results(request):
    query = request.GET['key']
    results = Search(query).results
    data = []
    for i in results:
        item = {
            'title': i.title,
            't_url': i.thumbnail_url,
            'watch_url': i.watch_url
        }
        data.append(item)

    return render(request, 'search_results.html', {'videos': data})

    


    
