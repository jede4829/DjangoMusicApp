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
    plot_div = Spotify_API.plotter(artist_stats.id)

    # return render(request,"search/do_search.html",{"r_name":artist_stats.spotify_name,"r_image":r_image,"r_genre":r_genres,"r_url":r_url,"r_follow":artist_stats.followers,"r_pop":artist_stats.popularity})
    context={"method": request.method,"plot_div": plot_div, "r_name":artist_stats.spotify_name,"r_image":r_image,"r_genre":r_genres,"r_url":r_url,"r_follow":artist_stats.followers,"r_pop":artist_stats.popularity }

    return render(request,"search/home.html",context)
    
def do_search_song(request):
    if request.method == "POST":
        song_name = request.POST["song"]
        client_id = request.POST["client_id"]
        client_secret = request.POST["client_secret"]
        track_stats = Spotify_API.Get_Song(song_name, client_id, client_secret)
    else:
        raise Http404("Invalid method for page")

    context = {"method": request.method, "r_name":track_stats.artist_name, "r_album":track_stats.album_url,  "r_album_title":track_stats.album_title,
               "r_song_url":track_stats.song_url, "r_song_name":track_stats.song_name, "r_song_popularity":track_stats.song_popularity, "r_song_track_number":track_stats.song_track_number}

    return render(request, "search/home.html", context)  # RETURN INFORMATION TO DIFFERENT PAGE THAN home.html WHICH IS FOR THE ARTIST.

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