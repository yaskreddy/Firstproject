from django.http import Http404
from django.http import HttpResponse
from .models import Album
from django.shortcuts import render, get_object_or_404
#from django.template import loader

def index(request):
    all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html')
    #context = {'all_albums':all_albums}
    return render (request,'music/index.html',{'all_albums':all_albums})
def detail(request,album_id):
    '''try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist :
        raise Http404("Album does not exist")'''
    #total try and except we will write in one line LANGUAGE_CODE
    album=get_object_or_404(Album,pk=album_id)
    return render (request,'music/detail.html',{'album':album})
def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render (request,'music/detail.html',{
        'album':album,
        'error_message' : "You did not select vaid song",
        })
    else:
        selected_song.is_favorite=True
        selected_song.save
        return render (request,'music/detail.html',{'album':album})
