from django.contrib import admin
from django.urls import include, path

from search.views import index
from search.views import newuser
from search.views import register
from search.views import home
from search.views import do_login
from search.views import do_search
<<<<<<< Updated upstream
from search.views import do_search_song
from search.views import add
=======
# from search.views import add
>>>>>>> Stashed changes
from search.views import logout_view

urlpatterns = [
    path('', index, name='index'),
    path('newuser', newuser, name='newuser'),
    path('register/', register, name='register'),
    path('home', home, name='home'),
    path('do_login/', do_login, name='do_login'),
    # path('add', add, name = 'add'),
    path('do_search/', do_search, name='do_search'),
    path('do_search_song/', do_search_song, name='do_search_song'),
    path('logout', logout_view, name='logout'),
]
