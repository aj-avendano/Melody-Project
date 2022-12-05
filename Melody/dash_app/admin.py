from django.contrib import admin

# Register your models here.
from dash_app.models import Playlist,PlaylistItems,UserPreferenceRecord,Genre,Artist,Album,Song

admin.site.register(Playlist)
admin.site.register(PlaylistItems)
admin.site.register(UserPreferenceRecord)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
