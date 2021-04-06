
from django.test import TestCase
from . import Spotify_API

artist = 'Halsey'
artist_test = Spotify_API.artist(artist)
artist_test.Get_Artist()
albums_test = Spotify_API.Get_Albums(artist_test.uri, 'album')
rec_albums_test = Spotify_API.Album_Generator(artist_test.id)
rec_songs_test = Spotify_API.Song_Generator(artist_test.id)
# audio_test = Spotify_API

artist_testing_set = True
album_testing_set = True
rec_album_testing_set = True
rec_songs_testing_set = True
# audio_testing_set = False
# song_search_test = False

class API_Test(TestCase):

	import requests
	import re

	if artist_testing_set:

		def test_artist_response(self):
			response_artist = artist_test
			self.assertTrue(response_artist)

		def test_artist_name(self):
			response_name = artist_test.spotify_name
			self.assertEqual(response_name, artist, 'Spotify API did not find artist chosen by user!')

		def test_artist_images(self):
			response_images = artist_test.images
			self.assertTrue(response_images)

		def test_artist_url(self):
			response_url = self.requests.get(artist_test.external_urls['spotify'])
			self.assertEqual(response_url.status_code, 200)

		def test_artist_uri(self):
			response_uri = self.re.findall(r"spotify[/:]*artist[/:]*[A-Za-z0-9]+", artist_test.uri)
			self.assertEqual(response_uri, [artist_test.uri])

	if album_testing_set:

		def test_album_response(self):
			response_album = albums_test
			self.assertTrue(response_album)

		def test_album_tracks(self):
			for k in range(0, len(albums_test)):
				if albums_test[k].tracks < 1:
					self.assertFalse(albums_test[k])
					break

		def test_album_images(self):
			for k in range(0, len(albums_test)):
				if not albums_test[k].images:
					self.assertFalse(albums_test[k].images)
					break

		def test_album_url(self):
			for k in range(0, len(albums_test)):
				response_url_album = self.requests.get(albums_test[k].url)
				if not response_url_album:
					self.assertFalse(response_url_album)
					break

		def test_album_uri(self):
			for k in range(0, len(albums_test)):
				test_uri_album = albums_test[k].uri
				response_uri_album = self.re.findall(r"spotify[/:]*album[/:]*[A-Za-z0-9]+", test_uri_album)
				if response_uri_album[0] != test_uri_album:
					self.assertFalse(response_uri_album)
					break

		def test_album_artist(self):
			for k in range(0, len(albums_test)):
				test_artist_album = albums_test[k].artist_name
				if test_artist_album != artist_test.spotify_name:
					self.assertFalse(test_artist_album)
					break

	if rec_album_testing_set:

		def test_rec_album_response(self):
			response_rec_album = rec_albums_test
			self.assertTrue(response_rec_album)

		def test_rec_album_tracks(self):
			for k in range(0, len(rec_albums_test)):
				if rec_albums_test[k].album_total_tracks < 1:
					self.assertFalse(rec_albums_test[k])
					break

		def test_rec_album_images(self):
			for k in range(0, len(rec_albums_test)):
				if not rec_albums_test[k].album_images:
					self.assertFalse(albums_test[k].album_images)
					break

		def test_rec_album_url(self):
			for k in range(0, len(rec_albums_test)):
				response_rec_url_album = self.requests.get(rec_albums_test[k].album_external_url['spotify'])
				if not response_rec_url_album:
					self.assertFalse(response_rec_url_album)
					break

		def test_rec_album_uri(self):
			for k in range(0, len(rec_albums_test)):
				test_rec_uri_album = rec_albums_test[k].album_uri
				response_rec_uri_album = self.re.findall(r"spotify[/:]*album[/:]*[A-Za-z0-9]+", test_rec_uri_album)
				if response_rec_uri_album[0] != test_rec_uri_album:
					self.assertFalse(response_rec_uri_album)
					break

		def test_rec_album_artists(self):
			artists = []
			for k in range(0, len(rec_albums_test)):
				artists.append(rec_albums_test[k].artist_name)
			if len(set(artists)) <= 1:
				self.assertFalse(len(set(artists)))

	if rec_songs_testing_set:

		def test_rec_songs_response(self):
			response_rec_songs = rec_songs_test
			self.assertTrue(response_rec_songs)

		def test_rec_songs_uri(self):
			for k in range(0, len(rec_songs_test)):
				test_rec_uri_songs = rec_songs_test[k].song_uri
				response_rec_uri_songs = self.re.findall(r"spotify[/:]*track[/:]*[A-Za-z0-9]+", test_rec_uri_songs)
				if response_rec_uri_songs[0] != test_rec_uri_songs:
					self.assertFalse(response_rec_uri_songs)
					break

		def test_rec_songs_url(self):
			for k in range(0, len(rec_songs_test)):
				response_rec_url_songs = self.requests.get(rec_songs_test[k].song_url)
				if not response_rec_url_songs:
					self.assertFalse(response_rec_url_songs)
					break

		def test_rec_songs(self):
			songs = []
			for k in range(0, len(rec_songs_test)):
				songs.append(rec_songs_test[k].song_name)
			if len(songs) <= 1:
				self.assertFalse(len(songs))

		def test_rec_songs_track_album(self):
			for k in range(0, len(rec_songs_test)):
				if not rec_songs_test[k].album_uri or not rec_songs_test[k].track_number:
					self.assertFalse(rec_songs_test[k])

		def test_rec_songs_track_ID(self):
			for k in range(0, len(rec_songs_test)):
				if rec_songs_test[k].song_id not in rec_songs_test[k].song_uri:
					self.assertFalse(rec_songs_test[k])

	# if audio_testing_set: