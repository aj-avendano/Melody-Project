from django.shortcuts import render

##Function Written by Jason Eissayou
def dashboard(request):
	return render(request, 'dashboard.html',{})
