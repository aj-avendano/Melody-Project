from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dash_app.models import Playlist,PlaylistItems,UserPreferenceRecord,Genre,Artist,Album,Song
from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm

#all forms classes were not in original class digram
#since at the time we were not aware that this method of using
#auto generated forms allowed for better structure and performance of our system
#(Anthony)

#Controller(playlistGeneratorform)
class CreateNewList(forms.Form):#Class Authorship: Jaimit
    # name = forms.CharField(label="Name...", max_length=100)
    Genre = forms.CharField(label="Genre:", max_length=100, required=False)
    Artist = forms.CharField(label="Artist:", max_length=100, required=False)
    Song = forms.CharField(label="Song:", max_length=100, required=False)

#Controller(UserCreationForm)
class NewUserForm(UserCreationForm):#Class Authorship:kuldeep
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
#Controller(createplaylistform)
class PlaylistForm(BSModalModelForm):#Class Authorship: Anthony Avendano
	class Meta:
		model = Playlist
		fields = ['playlist_title']
#Controller(CreatePlaylistItems)
class PlaylistItemsForm(BSModalModelForm):#Class Authorship: Anthony Avendano
	class Meta:
		model = PlaylistItems
		fields = ['playlist','artist','album','song']
#Controller(CreateUserPreferenceForm)
class UserPreferenceForm(BSModalModelForm): # Class Authorship: Anthony Avendano and Joaquin Johnson
	class Meta:
		model = UserPreferenceRecord
		fields = ['genre', 'artist', 'song']
