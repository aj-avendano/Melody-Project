from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Playlist(models.Model):#class by Anthony
    user = models.ForeignKey(User,on_delete=models.CASCADE)#One(profile)To Many Playlist relationship
    playlist_title = models.CharField(max_length=25)

class PlaylistItems(models.Model):#class by Anthony
    playlist=models.ForeignKey(Playlist,on_delete=models.CASCADE)#One(Playlist)To Many PlaylistItems relationship
    song=models.CharField(max_length=25)
    artist =models.CharField(max_length=25)
    album=models.CharField(max_length=25)
#Test script
#/Melody>python manage.py migrate
#/Melody>>python manage.py makemigrations dash_app
#/Melody>python manage.py sqlmigrate dash_app 000i
#>>>from django.contrib.auth.models import User
#>>>from dash_app.models import Profile, Playlist, PlaylistItems
class UserPreferenceRecord(models.Model):#class by Anthony
    user=models.ForeignKey(User,on_delete=models.CASCADE)#One(profile)To Many FavoriteGenres relationship
    genre=models.CharField(max_length=30)
    artist=models.CharField(max_length=30)
    song=models.CharField(max_length=30)
#Test script
#/Melody>python manage.py migrate
#/Melody>>python manage.py makemigrations dash_app
#/Melody>python manage.py sqlmigrate dash_app 000i
#>>>from django.contrib.auth.models import User
#>>>from dash_app.models import FavoriteGenres, FavoriteArtist, FavoriteSong
class Genre(models.Model):#class by Jaimit
    genre_name = models.CharField(max_length=30)
class Artist(models.Model):#class by Jaimit
    name = models.CharField(max_length=25)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
class Album(models.Model):#class by Jaimit
    album_name = models.CharField(max_length=25)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
class Song(models.Model):#class by Jaimit
    Song_name = models.CharField(max_length=25)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
class SongLyrics(models.Model):#class by Jaimit
    lyrics = models.CharField(max_length=5000)
    song = models.OneToOneField(Song,on_delete=models.CASCADE)
    song_title=models.CharField(max_length=25)
    artist =models.CharField(max_length=25)
#Test script
#/Melody>python manage.py migrate
#/Melody>>python manage.py makemigrations dash_app
#/Melody>python manage.py sqlmigrate dash_app 000i
#>>>from dash_app.models import Genre, Artist, Song, ALbum, SongLyrics
