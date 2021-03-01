from django.contrib import admin
from django.urls import path

from music.views import music_list_view
from music.views import jelly_search_view


from music.views import jam_list_view
from music.views import album_list_view
from music.views import artist_list_view
from music.views import song_list_view
from music.views import track_list_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', jelly_search_view)
]
