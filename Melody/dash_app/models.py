from django.db import models

# Create your models here.
<<<<<<< HEAD
#music_record model attributes (song_title,artist,genre,lyrics,album,tags)
#abstract User

=======

class Database(models.Model): #Jaimit James
    MusicRecord = models.CharField(max_length=30)
    User = models.CharField(max_length=30)
    Playlist = models.CharField(max_length=30)

class Music_Record(models.Model): #Jaimit James
    genre = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    song_title = models.CharField(max_length=30)
    lyrics = models.CharField(max_length=30) # update model relationship
    tags = models.CharField(max_length=30) # update model relationship

class Playlist(models.Model): #Jaimit James
    title = models.CharField(max_length=25)
    songs = models.CharField(max_length=25)

class User(models.Model): #Jaimit James
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class User_Preferences(models.Model): #Jaimit James
    playlists = models.CharField(max_length=30) # model attribute
    favorite_genres = models.CharField(max_length=30) # model attribute
    favorite_artist = models.CharField(max_length=30) # model attribute
    favorite_songs = models.CharField(max_length=30) # model attribute
    
>>>>>>> 6439f88ff20ca924bfb54687cd505bd4c83bf6de
