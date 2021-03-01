
import spotipy
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

cid = '4bf3768559cb4d84b4ef2e37384030d9'
secret = '15081679c0e04eff9422f1463cda5f23'
client = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client)

def print_class(instance):
    keys = []
    class_var = instance.__dict__
    for k in class_var:
        keys.append(k)
    for j in keys:
        if type(class_var) is not str:
            print(j + ' :    ' + str(class_var[j]))
        else:
            print(j + ' :    ' + class_var[j])
    return None

def print_json(object):
    print(json.dumps(object, sort_keys = True, indent = 4))
    return None

def View_AllAlbums(album_class_list):
    for i in range(0, len(album_class_list)):
        print('ALBUM INDEX: ' + str(i) + '\n')
        print_class(album_class_list[i])
        print('\n')

def View_AllTracks(tracks_list):
    for i in range(0, len(tracks_list)):
        print('Track INDEX: ' + str(i) + '\n')
        print_class(tracks_list[i])
        print('\n')

class album:
    def __init__(self):
        self.href = ''
        self.uri = ''
        self.id = ''
        self.album_name = ''
        self.release_date = ''
        self.tracks = ''
        self.images = ''

class artist:
    def __init__(self, name):
        self.external_urls = ''
        self.uri = ''
        self.id = ''
        self.input_name = name
        self.spotify_name = ''
        self.followers = 0
        self.genres = ''
        self.popularity = 0
        self.href = ''
        self.images = ''

    def Artist_Profile(self, tp_art):
        self.external_urls = tp_art['external_urls']
        self.uri = tp_art['uri']
        self.id = tp_art['id']
        self.spotify_name = tp_art['name']
        self.followers = tp_art['followers']['total']
        self.genres = tp_art['genres']
        self.popularity = tp_art['popularity']
        self.href = tp_art['href']
        self.images = tp_art['images']

    def Get_Artist(self):
        results = sp.search(q='artist:' + self.input_name, type='artist')
        List_of_Artists = results['artists']
        Attributes_Artists = List_of_Artists['items']
        Top_Artist = Attributes_Artists[0]
        self.Artist_Profile(Top_Artist)

class song:
    def __init__(self):
        self.album_title = ''
        self.release_date = ''
        self.track_total = 0
        self.artist_name = ''
        self.disc_number = 0
        self.duration_ms = 0
        self.explicit = ''
        self.track_url = ''
        self.href = ''
        self.track_id = ''
        self.is_local = ''
        self.track_popularity = 0
        self.track_number = 0
        self.uri = ''

def Get_Albums(uri, type):
    album_titles, uris, hrefs, ids, tracks, rds, imgs = [], [], [], [], [], [], []
    album_ClassList = []
    artist_albums = sp.artist_albums(uri, album_type=type)
    available_albums = artist_albums['items']
    k = 0
    while k < len(available_albums):
        album_titles.append(available_albums[k]['name'])
        uris.append(available_albums[k]['uri'])
        hrefs.append(available_albums[k]['href'])
        ids.append(available_albums[k]['id'])
        tracks.append(available_albums[k]['total_tracks'])
        rds.append(available_albums[k]['release_date'])
        imgs.append(available_albums[k]['images'])
        album_stats = album()
        album_stats.href = available_albums[k]['href']
        album_stats.uri = available_albums[k]['uri']
        album_stats.id = available_albums[k]['id']
        album_stats.album_name = available_albums[k]['name']
        album_stats.release_date = available_albums[k]['release_date']
        album_stats.tracks = available_albums[k]['total_tracks']
        album_stats.images = available_albums[k]['images']
        album_ClassList.append(album_stats)
        del album_stats
        k += 1
    df = pd.DataFrame({'Album Name':album_titles, 'Release Date':rds, '# of Tracks':tracks, 'Spotify ID':ids, 'Spotify URI':uris, 'Spotify HREF':hrefs, 'Images':imgs})
    return df, album_ClassList

def Get_Song(track):
    song_stats = song()
    songs = sp.search(track, limit=3)
    single = songs['tracks']['items'][0]
    song_stats.album_title = single['album']['name']
    song_stats.release_date = single['album']['release_date']
    song_stats.track_total = single['album']['total_tracks']
    song_stats.artist_name = single['artists'][0]['name']
    song_stats.disc_number = single['disc_number']
    song_stats.duration_ms = single['duration_ms']
    song_stats.explicit = single['explicit']
    song_stats.track_url = single['external_urls']['spotify']
    song_stats.href = single['href']
    song_stats.track_id = single['id']
    song_stats.is_local = single['is_local']
    song_stats.track_popularity = single['popularity']
    song_stats.track_number = single['track_number']
    song_stats.uri = single['uri']
    return song_stats

class track:
    def __init__(self):
        self.disc_number = 0
        self.duration_ms = 0
        self.explicit = ''
        self.track_url = ''
        self.href = ''
        self.track_id = ''
        self.is_local = ''
        self.track_name = ''
        self.track_number = 0
        self.uri = ''

def Get_Album_Tracks(album_uri):
    dsc_num, dur, explicit, url, href, id, local, name, number, uri = [], [], [], [], [], [], [], [], [], []
    album_TrackList = []
    album_tracks_complete = sp.album_tracks(album_uri)
    all_tracks = album_tracks_complete['items']
    i = 0
    while i < len(all_tracks):
        dsc_num.append(all_tracks[i]['disc_number'])
        dur.append(all_tracks[i]['duration_ms'])
        explicit.append(all_tracks[i]['explicit'])
        url.append(all_tracks[i]['external_urls']['spotify'])
        href.append(all_tracks[i]['href'])
        id.append(all_tracks[i]['id'])
        local.append(all_tracks[i]['is_local'])
        name.append(all_tracks[i]['name'])
        number.append(all_tracks[i]['track_number'])
        uri.append(all_tracks[i]['uri'])
        track_stats = track()
        track_stats.disc_number = all_tracks[i]['disc_number']
        track_stats.duration_ms = all_tracks[i]['duration_ms']
        track_stats.explicit = all_tracks[i]['explicit']
        track_stats.track_url = all_tracks[i]['external_urls']['spotify']
        track_stats.href = all_tracks[i]['href']
        track_stats.track_id = all_tracks[i]['id']
        track_stats.is_local = all_tracks[i]['is_local']
        track_stats.track_name = all_tracks[i]['name']
        track_stats.track_number = all_tracks[i]['track_number']
        track_stats.uri = all_tracks[i]['uri']
        album_TrackList.append(track_stats)
        del track_stats
        i += 1
    df = pd.DataFrame({'Disc Number':dsc_num, 'Duration':dur, 'Explicit':explicit, 'Track URL':url, 'Spotify HREF':href, 'Spotify ID':id, 'Local':local, 'Track Number':number, 'Spotify URI':uri,})
    return df, album_TrackList

# 1 CHOOSE ARTIST AND PRINT CLASS
# ````````````````````````````````
artist_name = 'Metallica'
artist_stats = artist(artist_name)
artist_stats.Get_Artist()
# print_class(artist_stats)   # Remove comment to print artist profile

# 2 GET ALL ALBUMS
# ````````````````````````````````

df_albums, Albums = Get_Albums(artist_stats.uri, 'album')
# View_AllAlbums(Albums)   # Remove comment to print all albums.  Choose index for album of choice.

# 3 GET SONG (all of step 4 must be commented to run step 3...for now)
# ````````````````````````````````

# track = Get_Song('brown sugar')
# print_class(track)   # Remove comment to print song profile

# 3 GET ALL SONGS FROM AN ALBUM (all of step 3 must be commented to run step 4...for now)
# ````````````````````````````````

df_tracks, Tracks = Get_Album_Tracks(Albums[0].uri)   # insert album index from step 2 here
# View_AllTracks(Tracks)    # Remove comment to print all tracks
