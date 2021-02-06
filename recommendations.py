import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_playlist_tracks(sp, username, playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def print_playlist_tracks( tracks ):
    for track in tracks:
        artists=None
        track1=None
        id0=None
        
        for track_key in track:
            print(track_key)

            if track_key=="track":
                track0 = track[ track_key ]
                
                print( type( track0 ) )

                for track0_key in track0:
                    print("\t", track0_key)

                    if track0_key=="artists":
                        artists=track0[track0_key]
                    elif track0_key=="track":
                        track1=track0[track0_key]
                    elif track0_key=="id":
                        id0=track0[track0_key]


        print(artists)
        print(track1)
        print(id0)
        print("----------")


def main():

    client_id = ""
    client_secret = ""

    sp = spotipy.Spotify( auth_manager=SpotifyClientCredentials( client_id=client_id, client_secret=client_secret))

    username = "vmlu6vaqv7yfbdaq84bh10o5t"
    playlistID = "spotify:playlist:45KSViu24qjpZgbShpnJ11"
    
    #sp_playlist = sp.user_playlist_tracks(username, playlist_id=playlistID)
    #tracks = sp_playlist['items']
    
    #tracks = get_playlist_tracks( sp, username, playlistID )
    #print_playlist_tracks(tracks)

    id_queen = "1dfeR4HaWDbWqFHLkxsg1d" 
    id_katyperry = "6jJ0s89eD6GaHleKKya26X"
    id_kmfdm = "3V4IvzRQYP5mzuVtkcHgVa"
    id_taylorswift = "06HL4z0CvFAxyc27GXpf02"
    id_metallica = "2ye2Wgw4gimLv2eAKyk1NB"

    result_amount = 5

    artist_list = [ id_queen, id_katyperry, id_kmfdm, id_taylorswift, id_metallica ]
    results = sp.recommendations(seed_artists=artist_list)
    
    for key in results:
        entry=results[key]
        if key=="tracks":
            for track in entry:
                for track_key in track:
                    track_val = track[track_key]
                    if track_key=="artists":
                        artists=track_val
                        for artist in artists:
                            print(f"{artist['name']}")
                            print(f"{artist['id']}")
                    if track_key=="name":
                        print(f"{track_key}: {track_val}")
                print()
        else:
            print(f"{key}: {entry}")

    #print ( type( results) )
    #for key in results:
    #    print(key)

if __name__ == "__main__":
    main()
