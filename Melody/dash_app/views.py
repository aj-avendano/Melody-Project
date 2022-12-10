from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.views.generic import  ListView
from .models import Playlist,PlaylistItems,UserPreferenceRecord,Genre,Artist,Album,Song
from bootstrap_modal_forms.generic import BSModalCreateView,BSModalFormView
from .forms import PlaylistForm, UserPreferenceForm,CreateNewList,PlaylistItemsForm
from django.urls import reverse_lazy
from django.db.models import Q # new
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#Any 'added extra class' means that the class was not on report class diagram

#Created by Kuldeep
#Controller(Displayhomepage)
class homepage(ListView):
#This class is to Displays homepage
	model = Playlist
	template_name = 'dash_app/home.html'

# Created by Kuldeep
#Controller(Register page)added extra class
class RegisterRequest(View):
	#Get Method created by Kuldeep
	#It gets the register template and displays it to the user.
	def get(self,request):
		form = NewUserForm()
			#If login is unsuccessful the you will be redirected to register page.
		return render (request=request, template_name="dash_app/register.html", context={"register_form":form})
	#Post Method created by Kuldeep
	#IT get the data entered in the register form and then saves it into database
	def post(self,request):
		if request.method == "POST":
			form = NewUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				login(request, user)
				messages.success(request, "Registration successful." )
				#If signup is successful the you will be redirected to dashboard page.
				return redirect("dash_app:dashboardHome")
			messages.error(request, "Unsuccessful registration. Invalid information.")


#class made by Anthony
#Controller(Verify Login)
class LoginRequest(View):
#Class for login
	#Function made by Anthony
	def get(self, request):
		return render(request,'dash_app/login.html',{ 'form':AuthenticationForm })
	#Function created by Kuldeep
	def post(self, request):
		form=AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f'You are now logged in as {username}.')
				return redirect ('dash_app:dashboardHome')
			else:
				messages.error(request,'Invalid username or password.')
		else:
			messages.error(request,'Invalid username or password.')


#Created by Kuldeep
#Controller(LogOut)added extra class
class LogoutRequest(View):
#Class used for logging out
	# Created by Kuldeep
	def get(self,request):
		logout(request)
		messages.info(request, "You have successfully logged out.")
		#redirected to login page.
		return redirect("dash_app:login")


#Class created by Kuldeep
#Controller(dashboard)added extra class
@method_decorator(login_required, name='dispatch')
class dashboardHome(ListView):
	#This class is used to display Dashboard home
	model = Playlist
	template_name= 'dash_app/dashboardHome.html'

#Controller(ItemsInPlaylist)added extra class
#class by Anthony Avendano
class PlaylistItemView(ListView):
#This class is used to display items being added into the playlist
	model = PlaylistItems
	template_name= 'dash_app/add_playlist_item.html'

#Controller(Search) search attributes were made into diffrent classes since then
#music record entity was split into multiple classes
class SearchGenre(ListView):#class by Anthony and Jason
    model=Genre
    template_name='dash_app/search_results_genre.html'
	#function by Anthony and Jason
	def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Genre.objects.filter(Q(genre_name__icontains=query))
        return object_list

#Controller(Search)#added extra class
class SearchAlbum(ListView):#class by Jason
    model=Album
    template_name='dash_app/search_results_album.html'
	#function by Anthony and Jason
	def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Album.objects.filter(Q(album_name__icontains=query))
        return object_list

#Controller(Search)#added extra class
class SearchArtist(ListView):#class by Jason
    model=Artist
    template_name='dash_app/search_results_artist.html'
	#function by Anthony and Jason
	def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Artist.objects.filter(Q(name__icontains=query))
        return object_list

#Controller(Search)#added extra class
class SearchSong(ListView):#class by Jason
    model=Song
    template_name='dash_app/search_results_song.html'
	#function by Anthony and Jason
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Song.objects.filter(Q(Song_name__icontains=query))
        return object_list
#Controller(Search)#added extra class
class SearchArtistsInGenre(ListView):#class by Jaimit
    model=Artist
    template_name='dash_app/search_results_artist.html'
	#function by Anthony and Jaimit
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Artist.objects.filter(genre__genre_name__icontains=query)
        return object_list

#class by Anthony Avendano
#Controller(Create Playlist)
class PlayListCreateView(LoginRequiredMixin,BSModalCreateView):
#this class posts form that gets info to make playlist
#retrives form data sending ito to the db
    template_name = 'dash_app/playlistform.html'
    form_class = PlaylistForm
    success_message = 'Success: playlist was created.'
    success_url = reverse_lazy('dash_app:add_item')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Created by Kuldeep
#Controller(Display Playlist)
class DisplayPlaylistView(LoginRequiredMixin,BSModalCreateView):
    template_name = 'dash_app/displayPlaylist.html'
    form_class = PlaylistForm
    success_message = 'Success: playlist was created.'
    success_url = reverse_lazy('dash_app:dashboardHome')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#class by Anthony Avendano
#Controller(CreatePlaylist) added extra class:since the record attribute of
#create playlist was turned into a class it required its own form
class PlaylistItemsCreateView(BSModalCreateView):
#this class posts form that gets info to make add item to playlist
#retrives form data sending ito to the db
    template_name = 'dash_app/playlistItems.html'
    form_class = PlaylistItemsForm
    success_message = 'Success: item was added.'
    success_url = reverse_lazy('dash_app:add_item')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#Class Authorship: Joaquin Johnson
#Controller(UserPreference)
class UserPreferenceView(LoginRequiredMixin,BSModalCreateView):
#this class posts form that gets info to make add item to playlist and
#retrives form data sending ito to the db
    template_name = 'dash_app/preferences.html'
    form_class = UserPreferenceForm
    success_message = 'Success: preference was created.'
    success_url = reverse_lazy('dash_app:dashboard')

#controller(generator)added extra class
# Class created by Kuldeep
# This is used for display the generator form and get the entered data from it and then saving it to database
@method_decorator(login_required, name='dispatch')
class generator(View):
	# Function created by Jaimit
	# Modified by Kuldeep
	def get(self,request):
		form = CreateNewList()
		return render(request, template_name='dash_app/generator.html', context={"form":form})
	# Function created by Jaimit
	# Modified by Kuldeep
	def post(self,request):
		if request.method == "POST":
			form = CreateNewList(request.POST) #gets the entries like name..., genre etc.
			if form.is_valid():
				Genre = form.cleaned_data["Genre"]
				Artist = form.cleaned_data["Artist"]
				Song = form.cleaned_data["Song"]
				list1 = []
				list1.append(Genre) ##adds the name to the list but can't print it out from page
				list1.append(Artist)
				list1.append(Song)
			return HttpResponseRedirect("dashboardHome") #if entries valid returns to this page
