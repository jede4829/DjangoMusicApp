from django.shortcuts import render
from django.http      import HttpResponse, Http404
from django.shortcuts import render
from django.urls      import reverse
from django.views     import generic
from django.utils     import timezone
from django.template  import loader
from django.contrib.auth.models import User

def index(request):
    return render(request, "search/index.html", {})

def newuser(request):
    return render(request, "search/newuser.html", {})

def register(request):
    if request.method=="POST":
        username=request.POST["name"]
        password=request.POST["password"]
        client_id=request.POST["client_id"]
        client_secret=request.POST["client_secret"]
        # --------------------
        # TODO: 
        # --------------------
        # Need to actually perform registration here
        # --------------------
        user = User.objects.create_user(username, "", password)
        user.profile.client_id=client_id 
        user.profile.client_secret=client_secret
        user.save()
        context = {
            'user':user 
        }
        return render(request, "search/register.html", context)
    else:
        raise Http404("Invalid request method")

