Project Title:	JamJelly

Team Members:	Ted Thayer, Jenna Dean, Shelby Bearrows, Sean McCormick

-------------------------
TEST CASE 1:  
-------------------------

Use Case Name:		Search for an artist..

Description:		The Spotify API retrieves information on the musical artist chosen by the user.

Pre-conditions:		Spotify API should be able to capture Spotify site relevant information on artist:

`				`1. Artist class fully populated post API query.

`				`2. Artist name given by user matches artist name found by Spotify API query.

`				`3. Associated images of artist returned from Spotify.

`				`4. URL to Spotify site for artist is valid.

`				`5. Spotify URI is valid and meets filtering requirements of regular expression that tests it.

Test steps:		Steps taken to execute artist query of Spotify API.

`				`1. Navigate to /JamJelly/search/test\_API.py.

`				`2. Set boolean variable artist\_testing\_set = True.

`				`3. Execute the command: python C:/<Local Directory Path>/JamJelly/manage.py test

Expected result:	All five tests pass.

Actual result:		All five tests pass.

Status (Pass/Fail):	Pass

Notes:			Spotify\_API code needs to execute to perform information retrieval from Spotify API.

`				`artist = 'Halsey' # (example artist)

`				`artist\_test = Spotify\_API.artist(artist)

Post-conditions:	Artist class populated with Spotify API query information.

-------------------------
TEST CASE 2:
-------------------------

Use Case Name:		Search for all albums available on Spotify by artist.

Description:		The Spotify API retrieves all albums created by the musical artist chosen by the user.

Pre-conditions:		Spotify API should be able to capture Spotify site relevant information on albums by artist:

`				`1. Albums classes fully populated post API query.

`				`2. Every album contains at least on song (some albums may be singles).

`				`3. Associated images for each album, or single, returned from Spotify.

`				`4. URL to Spotify album sites from artist are valid.

`				`5. Spotify album URI's are valid and meet the filtering requirements of regular expression that test each of them.

`				`6. All albums confirmed to be from correct artist.

Test steps:		Steps taken to execute album query by original artist to Spotify API.

`				`1. Navigate to /JamJelly/search/test\_API.py.

`				`2. Set boolean variable album\_testing\_set = True.

`				`3. Execute the command: python C:/<Local Directory Path>/JamJelly/manage.py test

Expected result:	All six tests pass.

Actual result:		All six tests pass.

Status (Pass/Fail):	Pass

Notes:			Spotify\_API code needs to execute to perform information retrieval from Spotify API.

`				`artist = 'Halsey' # (example artist)

`				`artist\_test = Spotify\_API.artist(artist)

`				`albums\_test = Spotify\_API.Get\_Albums(artist\_test.uri, 'album')

Post-conditions:	A list of album classes populated with Spotify API query information.

-------------------------
TEST CASE 3:
-------------------------

Use Case Name:		Search for album recommendations on Spotify by various artists related to the original artist.

Description:		The Spotify API retrieves recommended albums created by various musical artists related to the original artist.

Pre-conditions:		Spotify API should be able to capture Spotify site relevant information on recommended albums by various artists:

`				`1. Recommended albums classes fully populated post API query.

`				`2. Every recommended album contains at least on song (some albums may be singles).

`				`3. Associated images for each recommended album, or single, returned from Spotify.

`				`4. URL's to recommended Spotify album sites from various artists are valid.

`				`5. Spotify recommended album URI's are valid and meet the filtering requirements of regular expression that test each of them.

`				`6. Verify multiple artists, apart from the original artist, returned as part of album recommendation.

Test steps:		Steps taken to execute recommended albums query by various artists related to the original artist to Spotify API.

`				`1. Navigate to /JamJelly/search/test\_API.py.

`				`2. Set boolean variable rec\_album\_testing\_set = True.

`				`3. Execute the command: python C:/<Local Directory Path>/JamJelly/manage.py test

Expected result:	All six tests pass.

Actual result:		All six tests pass.

Status (Pass/Fail):	Pass

Notes:			Spotify\_API code needs to execute to perform information retrieval from Spotify API.

`				`artist = 'Halsey' # (example artist)

`				`artist\_test = Spotify\_API.artist(artist)

`				`rec\_albums\_test = Spotify\_API.Album\_Generator(artist\_test.id)

Post-conditions:	A list of recommended album classes populated with Spotify API query information.

-------------------------
TEST CASE 4:
-------------------------

Use Case Name:		Retrieve song recommendations from Spotify by various artists related to the original artist.

Description:		This series of tests ensures that the Spotify API retrieves recommended songs created by various musical artists related to the original artist.

Pre-conditions:		Spotify API should be able to capture Spotify site relevant information on recommended songs by various artists:

`				`1. Spotify recommended songs URI's are valid and meet the filtering requirements of regular expression that test each of them.

`				`2. URL's to recommended Spotify song sites from various artist sare valid.

`				`3. At least five recommended songs should be received from Spotify.

`				`4. All recommended songs have an associated album and track number.

`				`5. The Spotify song ID for each recommended songs in embedded in the associated URI.

Test steps:		Steps taken to execute recommended songs query of Spotify API.

`				`1. Navigate to /JamJelly/search/test\_API.py.

`				`2. Set boolean variable rec\_songs\_test = True.

`				`3. Execute the command: python C:/<Local Directory Path>/JamJelly/manage.py test

Expected result:	All five tests pass.

Actual result:		All five tests pass.

Status (Pass/Fail):	Pass

Notes:			Spotify\_API code needs to execute to perform information retrieval from Spotify API.

`				`artist = 'Halsey' # (example artist)

`				`artist\_test = Spotify\_API.artist(artist)

`				`rec\_songs\_test = Spotify\_API.Song\_Generator(artist\_test.id)

Post-conditions:	A list of recommended songs classes populated with Spotify API query information.

-------------------------
TEST CASE 5:
-------------------------

Use Case Name:		Capture acoustic characteristics of each recommended song.

Description:		The Spotify API returns all the audio properties of each recommended song.

Pre-conditions:		Spotify API should be able to capture the audio characteristics of each recommended song:

`				`1. Validate that a dataframe was created to hold all acoustics features for every recommended song.

`				`2. Dataframe should not contain any zero entries.

`				`3. Dataframe should not contain any empty entries.

Test steps:		Steps taken to execute recommended songs query of Spotify API.

`				`1. Navigate to /JamJelly/search/test\_API.py.

`				`2. Set boolean variable audio\_testing\_set = True.

`				`3. Execute the command: python C:/<Local Directory Path>/JamJelly/manage.py test

Expected result:	All three tests pass.

Actual result:		All three tests pass.

Status (Pass/Fail):	FAIL (Not implemented yet)

Notes:			Spotify\_API code needs to execute to perform information retrieval from Spotify API.

`				`artist = 'Halsey' # (example artist)

`				`artist\_test = Spotify\_API.artist(artist)

`				`NOT IMPLEMENTED YET.

Post-conditions:	A dataframe populated with all the acoustic features of every recommended song is created.

-------------------------
TEST CASE 6:
-------------------------

Use Case Name:		Perform song search.

Description:		Search Spotify for information for a song input by the user.

Pre-conditions:		Spotify API should be able to show the user who performed a song:

`				`1. Validate artist\_ID.

`				`2. Validate song\_ID.

`				`3. URL to searched song is valid.

`				`4. URI to searched song is valid

Test steps:		Steps taken to execute recommended songs query of Spotify API.

`				`1. Navigate to /JamJelly/search/test\_API.py.

`				`2. Set boolean variable # song\_search\_test = True.

`				`3. Execute the command: python C:/<Local Directory Path>/JamJelly/manage.py test

Expected result:	All four tests pass.

Actual result:		All four tests pass.

Status (Pass/Fail):	FAIL (Not implemented yet)

Notes:			Spotify\_API code needs to execute to perform information retrieval from Spotify API.

`				`artist = 'Halsey' # (example artist)

`				`artist\_test = Spotify\_API.artist(artist)

`				`NOT IMPLEMENTED YET.

Post-conditions:	User is given artist information for searched song.

-------------------------
TEST CASE 7:
-------------------------

Use Case Name:		Verify JamJelly site functionality.

Description:		Perform basic checks into site functions (login, create new user, search for song, etc.).

Pre-conditions:		Views.py needs to have requisite functions built:

`				`1. Validate username and password.

`				`2. Validate site index and endpoint.

`				`3. Check new user registration and reverse user lookup.

`				`4. Check search and reverse search.

Test steps:		Steps taken to execute recommended songs query of Spotify API.

`				`1. Navigate to /JamJelly/search/tests.py.

`				`2. Set boolean variable # test\_urls = True.

`				`3. Execute the command: python C:/<Local Directory Path>/JamJelly/manage.py test

Expected result:	All 10 tests pass.

Actual result:		All 10 tests pass.

Status (Pass/Fail):	Pass (Sections of this test file still being implemented however.)

Notes:			Import the following:

`				`from django.test import TestCase, Client

`				`from django.urls import reverse

`				`from . import views

`				`from django.http import HttpRequest

Post-conditions:	All site functions confirmed to work properly.

-------------------------
TEST CASE 8:
-------------------------

Use Case Name:		Site user login and authentication.

Description:		Perform checks on JamJelly site user creation and authentication.

Pre-conditions:		models.py needs to have requisite functions built:

`				`1. create user with client ID and client secret.

Test steps:		Steps taken to execute recommended songs query of Spotify API.

`				`1. Navigate to /JamJelly/search/test\_models.py.

`				`2. Set boolean variable # test\_models = True.

`				`3. Execute the command: python C:/<Local Directory Path>/JamJelly/manage.py test

Expected result:	All seven tests pass.

Actual result:		All seven tests pass.

Status (Pass/Fail):	Pass

Notes:			Import the following:

`				`from django.test import TestCase

`				`from django.contrib.auth.models import User

`				`from django.contrib.auth import authenticate, login

`				`from search.models import Profile

Post-conditions:	Attempted logins for new user succeed or fail based on username and password pair variations.
