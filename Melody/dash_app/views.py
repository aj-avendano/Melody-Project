from django.shortcuts import  render, redirect,reverse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import  ListView, DetailView,TemplateView
from dash_app.models import Playlist,PlaylistItems,UserPreferenceRecord,Genre,Artist,Album,Song
from bootstrap_modal_forms.generic import BSModalCreateView,BSModalFormView
from dash_app.forms import PlaylistForm, UserPreferenceForm,CreateNewList,PlaylistItemsForm
from django.urls import reverse_lazy
from django.db.models import Q # new
from django.contrib.auth.mixins import LoginRequiredMixin


class SearchGenre(ListView):
    model=Genre
    template_name='dash_app/search_results_genre.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Genre.objects.filter(Q(genre_name__icontains=query))
        return object_list
class SearchAlbum(ListView):
    model=Album
    template_name='dash_app/search_results_album.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Album.objects.filter(Q(album_name__icontains=query))
        return object_list
class SearchArtist(ListView):
    model=Artist
    template_name='dash_app/search_results_artist.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Artist.objects.filter(Q(name__icontains=query))
        return object_list
class SearchSong(ListView):
    model=Song
    template_name='dash_app/search_results_song.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Song.objects.filter(Q(Song_name__icontains=query))
        return object_list

class SearchArtistsInGenre(ListView):
    model=Artist
    template_name='dash_app/search_results_artist.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list= Artist.objects.filter(genre__genre_name__icontains=query)
        return object_list

class PlayListCreateView(LoginRequiredMixin,BSModalCreateView):
    template_name = 'dash_app/playlistform.html'
    form_class = PlaylistForm
    success_message = 'Success: playlist was created.'
    success_url = reverse_lazy('dash_app:dashboard')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaylistItemsCreateView(BSModalCreateView):
    template_name = 'dash_app/playlistform.html'
    form_class = PlaylistItemsForm
    success_message = 'Success: item was added.'
    success_url = reverse_lazy('dash_app:dashboard')

class UserPreferenceView(LoginRequiredMixin,BSModalCreateView):
    template_name = 'dash_app/preferences.html'
    form_class = UserPreferenceForm
    success_message = 'Success: preference was created.'
    success_url = reverse_lazy('dash_app:dashboard')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



##Function Written by Jason Eissayou
#def dashboard(request):
#	return render(request=request, template_name='dash_app/dashboard.html')

#Function created Kuldeep
def homepage(request):
	#takes you to he home page
	return render(request=request, template_name='dash_app/home.html')

#Function created Kuldeep
#Function for register
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			#If signup is successful the you will be redirected to dashboard page.
			return redirect("dash_app:dashboardHome")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	#If login is unsuccessful the you will be redirected to register page.
	return render (request=request, template_name="dash_app/register.html", context={"register_form":form})


#Class for login
#class made by Anthony
class LoginRequest(View):
	#Function made by Anthony
	def get(self, request):
		return render(request,'dash_app/login.html',{ 'form':AuthenticationForm })
	#Function created Kuldeep
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

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	#redirected to login page.
	return redirect("dash_app:login")

def dashboardHome(request):

	return render(request=request, template_name='dash_app/dashboardHome.html')


def preferences(request):

	return render(request=request, template_name='dash_app/preferences.html')

def generator(request):

	return render(request=request, template_name='dash_app/generator.html')
def playlist(request):
	return render(request=request, template_name='dash_app/testsearch.html')

def generator(request): #Jaimit
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

	else:
		form = CreateNewList()

	return render(request, template_name='dash_app/generator.html', context={"form":form})
