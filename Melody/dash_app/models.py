from django.db import models
from django.contrib.auth.models import User#Entity(User)
# database object relational models
# each class represents an entity and a table in our databse
#Entity(Playlist)
class Playlist(models.Model):#class by Joaquin Johnson  Anthony
    user = models.ForeignKey(User,on_delete=models.CASCADE)#One(profile)To Many Playlist relationship
    playlist_title = models.CharField(max_length=25, null=True)
    def __str__(self):
        return self.playlist_title
#Entity(Song record) this entity was made from the playlist entity class
#this was done in order to attach song records to playlist by foreign key since
#list field type is not valid in sql lite (Anthony)
class PlaylistItems(models.Model):#class by Joaquin Johnson and Anthony
    playlist=models.ForeignKey(Playlist,on_delete=models.CASCADE)#One(Playlist)To Many PlaylistItems relationship
    song=models.CharField(max_length=25, null=True)
    artist =models.CharField(max_length=25, null=True)
    album=models.CharField(max_length=25, null=True)
    def __str__(self):
        return self.song
#Test script(Anthony)
#/Melody>python manage.py migrate
#/Melody>>python manage.py makemigrations dash_app
#/Melody>python manage.py sqlmigrate dash_app 000i
#>>>from django.contrib.auth.models import User
#>>>from dash_app.models import Playlist, PlaylistItems

#(Anthony)Entity(Music Record): the entity of Music record was split into
#several classes according to its attributes instead of one whole class
#this was done in order to have an easier way of querying the database for records
class Genre(models.Model):#class by Jaimit and Anthony
    genre_name = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.genre_name
#Entity(Music Record)
class Artist(models.Model):#class by Jaimit and Anthony
    name = models.CharField(max_length=25, null=True)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
#Entity(Music Record)
class Album(models.Model):#class by Jaimit and Anthony
    album_name = models.CharField(max_length=25, null=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    def __str__(self):
        return self.album_name
#Entity(Music Record)
class Song(models.Model):#class by Jaimit and Anthony
    Song_name = models.CharField(max_length=25, null=True)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    def __str__(self):
        return self.Song_name
#Entity(Music Record)
class SongLyrics(models.Model):#class by Jaimit and Anthony
    lyrics = models.CharField(max_length=5000, null=True)
    song = models.OneToOneField(Song,on_delete=models.CASCADE)
    song_title=models.CharField(max_length=25, null=True)
    artist =models.CharField(max_length=25, null=True)
#Test script(Anthony)
#/Melody>python manage.py migrate
#/Melody>>python manage.py makemigrations dash_app
#/Melody>python manage.py sqlmigrate dash_app 000i
#>>>from django.contrib.auth.models import User
#>>>from dash_app.models import SongLyrics,Genre,Artist,Song,Album

#Entity(User preference)
class UserPreferenceRecord(models.Model): #class by Joaquin Johnson and Anthony
    user=models.ForeignKey(User,on_delete=models.CASCADE)#One(user)To Many preferences relationship
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    artist=models.CharField(max_length=25, null=True)
    song=models.CharField(max_length=25, null=True)
#Test script(Anthony)
#/Melody>python manage.py migrate
#/Melody>>python manage.py makemigrations dash_app
#/Melody>python manage.py sqlmigrate dash_app 000i
#>>>from dash_app.models import UserPreferenceRecord
