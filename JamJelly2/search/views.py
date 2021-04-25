from django.shortcuts import render
from django.http      import HttpResponse, Http404
from django.shortcuts import render, HttpResponseRedirect
from django.urls      import reverse
from django.views     import generic
from django.utils     import timezone
from django.template  import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from . import Spotify_API

def add(request):
    val = str(request.POST["forminfo"])   ###  INSERT SPOTIFY API HERE
    return render(request,"search/output.html",{"output":val})

def index(request):
    return render(request, "search/index.html", {})

def newuser(request):
    return render(request, "search/newuser.html", {})

def home(request):
    if request.user.is_authenticated:
        context = {
            'user':request.user
        }
        return render(request, "search/home.html", context)
    else:
        raise Http404("User is not logged in!")

def do_login(request):
    if request.method=="POST":

        username=request.POST["name"]
        password=request.POST["password"]

        print(f"username: [{username}]")
        print(f"password: [{password}]")

        user = authenticate(request, username=username, password=password )

        print(f"user: {user}")

        if user is not None:
            print("user is not None")
            # auth'd
            login(request, user)
            #return HttpResponseRedirect('/search/home')
            return HttpResponseRedirect('/home')
        else:
            print("user is None")
            raise Http404("Failed to login")
            # not-auth'd
        #return home(request)
    print("invalid method for do_login")
    raise Http404("Invalid method for page")

def do_search(request):
    print("do_search")
    if request.method == "POST":
        artist_name = request.POST["artist"]

        if artist_name == "" or artist_name.strip() == "":
            #raise Http404("Search cannot be empty")
            return render(request,"search/home.html",{'error':'search cannot be empty'})

        client_id = request.POST["client_id"]
        client_secret = request.POST["client_secret"]

        artist_stats = Spotify_API.artist(artist_name, client_id, client_secret)
        artist_stats.Get_Artist()
    else:
        raise Http404("Invalid method for page")

    r_genres = str(artist_stats.genres).replace("[","").replace("]","")
    r_url = str(artist_stats.external_urls).replace("{'spotify': '","").replace("'}","")
    r_image = str(artist_stats.images[0]).split("'url': '",1)[1].split("', '",1)[0]
    plot_div = Spotify_API.plotter(artist_stats)

    # return render(request,"search/do_search.html",{"r_name":artist_stats.spotify_name,"r_image":r_image,"r_genre":r_genres,"r_url":r_url,"r_follow":artist_stats.followers,"r_pop":artist_stats.popularity})
    context={"method": request.method,"plot_div": plot_div, "r_name":artist_stats.spotify_name,"r_image":r_image,"r_genre":r_genres,"r_url":r_url,"r_follow":artist_stats.followers,"r_pop":artist_stats.popularity }

    return render(request,"search/home.html",context)

def do_search_song(request):
    if request.method == "POST":
        # song_name = request.POST["song"]
        song_name = request.POST["artist"]
        client_id = request.POST["client_id"]
        client_secret = request.POST["client_secret"]
        track_stats = Spotify_API.Get_Song(song_name, client_id, client_secret)
        artist_stats = Spotify_API.artist(track_stats.artist_name, client_id, client_secret)
        artist_stats.Get_Artist()
        r_image = str(artist_stats.images[0]).split("'url': '",1)[1].split("', '",1)[0]
        # ------- Recommended Songs -------
        artist_stats = Spotify_API.artist(track_stats.artist_name, client_id, client_secret)
        artist_stats.Get_Artist()
        recommended_songs = Spotify_API.Song_Generator(artist_stats.id)
        song1 = recommended_songs[0]
        song2 = recommended_songs[1]
        song3 = recommended_songs[2]
        song4 = recommended_songs[3]
        song5 = recommended_songs[4]

    else:
        raise Http404("Invalid method for page")

    context = {"method": request.method, "r_image":r_image, "r_song_name":song_name, "r_artist_name":track_stats.artist_name, "r_url":track_stats.track_url,  "r_album_title":track_stats.album_title,
               "r_date":track_stats.release_date, "r_pop":track_stats.track_popularity, "r_duration":(track_stats.duration_ms/60000),
               "1_song":song1.song_name, "2_song":song2.song_name, "3_song":song3.song_name, "4_song":song4.song_name, "5_song":song5.song_name,
               "1_song_url":song1.song_url, "2_song_url":song2.song_url, "3_song_url":song3.song_url, "4_song_url":song4.song_url, "5_song_url":song5.song_url}

    return render(request, "search/home.html", context)  # RETURN INFORMATION TO DIFFERENT PAGE THAN home.html WHICH IS FOR THE ARTIST.

def do_recommended_songs(request):
    artist_name = request.POST["artist"]
    if artist_name == "" or artist_name.strip() == "":
        return render(request,"search/home.html",{'error':'search cannot be empty'})
    client_id = request.POST["client_id"]
    client_secret = request.POST["client_secret"]
    artist_stats = Spotify_API.artist(artist_name, client_id, client_secret)
    artist_stats.Get_Artist()
    recommended_songs = Spotify_API.Song_Generator(artist_stats.id)
    song1 = recommended_songs[0]
    song2 = recommended_songs[1]
    song3 = recommended_songs[2]
    song4 = recommended_songs[3]
    song5 = recommended_songs[4]
    context = {"method": request.method, "1_song":song1, "2_song":song2, "3_song":song3, "4_song":song4, "5_song":song5}
    return render(request, "search/home.html", context)

def do_recommended_albums(request):
    artist_name = request.POST["artist"]
    if artist_name == "" or artist_name.strip() == "":
        return render(request,"search/home.html",{'error':'search cannot be empty'})
    client_id = request.POST["client_id"]
    client_secret = request.POST["client_secret"]
    artist_stats = Spotify_API.artist(artist_name, client_id, client_secret)
    artist_stats.Get_Artist()
    recommended_albums = Spotify_API.Album_Generator(artist_stats.id)
    album1 = recommended_albums[0]
    album2 = recommended_albums[1]
    album3 = recommended_albums[2]
    album4 = recommended_albums[3]
    album5 = recommended_albums[4]
    context = {"method": request.method, "1_album":album1, "2_album":album2, "3_album":album3, "4_album":album4, "5_album":album5}
    return render(request, "search/home.html", context)

def register(request):
    if request.method=="POST":
        username=request.POST["name"]
        password=request.POST["password"]
        client_id=request.POST["client_id"]
        client_secret=request.POST["client_secret"]

        if client_id=="":
            raise Http404("Please fill in client_id field.")
        if client_secret=="":
            raise Http404("Please fill in client_secret field.")

        if username=="":
            raise Http404("Username cannot be an empty string")

        if check_password(password)==False:
            raise Http404("Password failed one or more conditions, please try again")

        print(f"Password: [{password}]")
        # --------------------
        # TODO:
        # --------------------
        # Need to actually perform registration here
        # --------------------
        try:
            #user = User.objects.create_user(username, "", password)
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.profile.client_id=client_id
            user.profile.client_secret=client_secret
            user.save()
            context = {
                'user':user
            }
            return render(request, "search/register.html", context)
        except Exception as e:
            raise Http404(e)
    else:
        raise Http404("Page cannot be accessed via GET method, please use the New User Registration Form")

def check_password(password):
    PasswordMinimumLength = 8
    if password=="":
        raise Http404("Password cannot be an empty string!")
    if len(password) < PasswordMinimumLength:
        raise Http404(f"Password must be at least {PasswordMinimumLength} characters!")
    hasUpper = False
    hasLower = False
    hasNumeric = False
    hasSpecial = False
    for c in password:
        if c.isupper():
            hasUpper=True
        if c.islower():
            hasLower=True
        if c.isnumeric():
            hasNumeric=True
        if c in "`~!@#$%^&*()_-+=[{]}\\|;:'\",<.>/?":
            hasSpecial=True
    return hasUpper and hasLower and hasNumeric and hasSpecial

def logout_view(request):
    logout(request)
    return render(request, "search/index.html", {})

    # Redirect to a success page
