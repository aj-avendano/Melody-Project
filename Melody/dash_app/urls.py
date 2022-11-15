from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "dash_app"

##Function Written by Jason Eissayou and Kuldeep
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path('login', views.LoginRequest.as_view(), name='login'),
    path("logout", views.logout_request, name= "logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('dashboardHome', views.dashboardHome, name="dashboardHome"),
    path('preferences', views.preferences, name="preferences"),
    path('generator', views.generator, name="generator")
]

urlpatterns += staticfiles_urlpatterns()
