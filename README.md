# TITLE: DjangoMusicApp
Software Class

-----
Team Members:


-----

## OVERVIEW

-----

**Motivation:** 

To allow a user to search for an artist and get not only top artist tracks, but also recommendations. 

**User-story:**

A user named Mike, for example, creates account on music app, logs in, at dashboard is asked to go to developers.spotify.com and acquire a client id and client secret.

On the dashboard (or in an optional settings screen), user puts the client id and client secret and clicks "save"
Client id and secret are stored encrypted in user's row in user table
At this point, user can search for a given artist and get:
    - top tracks
    - recommendations
- Top tracks
    Top tracks returns a list in a table-format
- Recommendations
    Returns a table of tracks
**Developement Method:**
- Django for web development framework
- Python

-----
## Project Tracking Todo list
1. caching the returned `artist_ids` so that we are not making redundant calls
1a. instead of performing a web request first, instead check the cache to see if a given artist and their id exist,
    if not, then perform a web request
1b. also want to cache the track ids returned by recommendations along with other info (like what artist the user initially searched for)
1c. In Django, we will want to integrate any database functionality that we develop here over there
    - The Django models file describes row-structures on a per-table basis
      Chances are that you will have a table for artist information

2. when we get our first generation of recommendations, we want to present the user with a chance to select which songs they like the most in order to seed further calls to recommendations. We can do this by adding a number in front of each track and then asking the user to enter the numbers matching their preferred tracks. 

3. Django-implementation
    - user login
    - on the user dashboard, a searchbox to search for an artist and get a list of the top 10 tracks for that artists maybe with links to their spotify page

4. User-specific `client_id` and `client_secret`
    - settings-page -or- put on dashboard that provides two textboxes and directions on how to get the `client_id` and `client_secret`

5. Two buttons:
    - `get_recommendations`
    - `top_tracks`

6. List link result format:
    [ artist ] - [ track name ] - [ spotify link ] 
    Something like...
    <a href="https://myapp.com/search?q={{% artist %}}">{{% artist %}}</a> 

7. CSS for the Django templates (*not required*)

8. Possible fields for getrecommendations (*not required*):
    - Tempo
    - Energy
    - etc

9. Encryption of user information in the database besides password
    - clientid
    - clientsecret
## Risks/Mitigation

-The time it will take to implement the technology to have a fully functional web app that generates an artist top tracks and recommendations
-Mitigate risks by dividing tasks among group members and checking in frequently. 

