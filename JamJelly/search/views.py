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

from . import module

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

        #print(f"username: [{username}]")
        #print(f"password: [{password}]")

        user = authenticate(request, username=username, password=password )
        if user is not None:
            # auth'd
            login(request, user)
            #return HttpResponseRedirect('/search/home')
            return HttpResponseRedirect('/home')
        else:
            raise Http404("Failed to login")
            # not-auth'd
        #return home(request)
    raise Http404("Invalid method for page")


def do_search(request):
    if request.method == "POST":
        artist_name = request.POST["artist"]
        client_id = request.POST["client_id"]
        client_secret = request.POST["client_secret"]

        artist_stats = module.artist(artist_name, client_id, client_secret)
        artist_stats.Get_Artist()

        # Jenna, choose any or multiple of the r_'s below.  Once you are okay with this implementation I will do the rest.

        # artist_stats = module.artist(artist_name, client_id, client_secret)
        # artist_stats.Get_Artist()
        # r_external_urls = module.get_str_class(artist_stats.external_urls)
        # r_uri = module.get_str_class(artist_stats.uri)
        # r_id = module.get_str_class(artist_stats.id)
        # r_spotify_name = module.get_str_class(artist_stats.spotify_name)
        # r_followers = module.get_str_class(artist_stats.followers)
        # r_genres = module.get_str_class(artist_stats.genres)
        # r_popularity = module.get_str_class(artist_stats.popularity)
        # r_href = module.get_str_class(artist_stats.href)
        # r_images = module.get_str_class(artist_stats.images)
        #
        # raise Http404(f"r: [{r}]")
    else:
        raise Http404("Invalid method for page")

    r_genres = str(artist_stats.genres).replace("[","").replace("]","")
    r_url = str(artist_stats.external_urls).replace("{'spotify': '","").replace("'}","")
    r_image = str(artist_stats.images[0]).split("'url': '",1)[1].split("', '",1)[0]

    # return render(request,"search/do_search.html",{"r_name":artist_stats.spotify_name,"r_image":r_image,"r_genre":r_genres,"r_url":r_url,"r_follow":artist_stats.followers,"r_pop":artist_stats.popularity})
    context={"method": request.method, "r_name":artist_stats.spotify_name,"r_image":r_image,"r_genre":r_genres,"r_url":r_url,"r_follow":artist_stats.followers,"r_pop":artist_stats.popularity }

    return render(request,"search/home.html",context)
    


#return render(request, "search/home.html", {})


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
            user = User.objects.create_user(username, "", password)
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