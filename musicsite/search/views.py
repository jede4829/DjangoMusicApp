from django.shortcuts import render
from django.http      import HttpResponse, Http404
from django.shortcuts import render, HttpResponseRedirect
from django.urls      import reverse
from django.views     import generic
from django.utils     import timezone
from django.template  import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

        user = authenticate(request, username=username, password=password ) 
        if user is not None:
            # auth'd
            login(request, user)
            return HttpResponseRedirect('/search/home')
        else:
            raise Http404("Failed to login")
            # not-auth'd
        return home(request)
    raise Http404("Invalid method for page")


    

#return render(request, "search/home.html", {})



def register(request):
    if request.method=="POST":
        username=request.POST["name"]
        password=request.POST["password"]
        client_id=request.POST["client_id"]
        client_secret=request.POST["client_secret"]

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







































