from django.contrib import admin

# Register your models here.
from .models import Jelly
from .models import Jam
from .models import Album
from .models import Artist
from .models import Song
from .models import Track

admin.site.register(Jelly)
admin.site.register(Jam)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Track)
