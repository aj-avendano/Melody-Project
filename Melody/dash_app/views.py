from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

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

#Function created Kuldeep 
#Function for login
def login_request(request):
	
	if request.method == "POST":	

		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				#If login is successful the you will be redirected to dashboard page. 
				return redirect ("dash_app:dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	#If login is unsuccessful the you will be redirected to login  page. 
	return render(request=request, template_name="dash_app/login.html", context={"login_form":form})
	#Function for logout
	
#Function created Kuldeep 
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	#redirected to login page. 
	return redirect("dash_app:login")