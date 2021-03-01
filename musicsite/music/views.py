from django.shortcuts import render
from .models import Jelly
from .models import Jam
from .models import Album
from .models import Artist
from .models import Song
from .models import Track

from .forms import JellyForm

# List Music information
def music_list_view(request):
    #Dictionary
    music_objects = Jelly.objects.all()
    context = {
        'music_objects': music_objects
    }
    return render(request, "music/index.html", context)

# Search information
def jelly_search_view(request):
    form = JellyForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "music/index.html",context)





#----------------------------------------

# List General Jam information
def jam_list_view(request):
    #Dictionary
    jam_objects = Jam.objects.all()
    context = {
        'jam_objects': jam_objects
    }
    return render(request, "music/index.html", context)

# List Album information
def album_list_view(request):
    #Dictionary
    album_objects = Album.objects.all()
    context = {
        'album_objects': album_objects
    }
    return render(request, "music/index.html", context)

# List Artist information
def artist_list_view(request):
    #Dictionary
    artist_objects = Artist.objects.all()
    context = {
        'artist_objects': artist_objects
    }
    return render(request, "music/index.html", context)

# List Song information
def song_list_view(request):
    #Dictionary
    song_objects = Song.objects.all()
    context = {
        'song_objects': song_objects
    }
    return render(request, "music/index.html", context)

# List Track information
def track_list_view(request):
    #Dictionary
    track_objects = Track.objects.all()
    context = {
        'track_objects': track_objects
    }
    return render(request, "music/index.html", context)
