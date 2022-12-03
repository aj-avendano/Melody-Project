from django.shortcuts import  render, redirect,reverse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import PermissionDenied
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from dash_app.models import Playlist,PlaylistItems,UserPreferenceRecord,Genre,Artist,Album,Song
from bootstrap_modal_forms.generic import BSModalCreateView
from dash_app.forms import PlaylistForm
from django.urls import reverse_lazy



class PlayListCreateView(BSModalCreateView):
    template_name = 'dash_app/playlistform.html'
    form_class = PlaylistForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('test')

class UserPreferenceView(BSModalCreateView): # class by Joaquin Johnson
    template_name = 'dash_app/preferences.html'
    form_class = UserPreferenceForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('test')

##Function Written by Jason Eissayou
def dashboard(request):
	return render(request=request, template_name='dash_app/dashboard.html')

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
			return redirect("dash_app:dashboard")
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
				return redirect ('dash_app:dashboard')
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
	return render(request=request, template_name='dash_app/test.html')
