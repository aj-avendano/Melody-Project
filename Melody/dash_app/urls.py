from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "dash_app"

##Function Written by Jason Eissayou and Kuldeep and Joaquin
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path('login', views.LoginRequest.as_view(), name='login'),
    path("logout", views.logout_request, name= "logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('dashboardHome', views.dashboardHome, name="dashboardHome"),
    path('preferences', views.preferences, name="preferences"),
    path('generator', views.generator, name="generator"),
    path('create_book', views.PlayListCreateView.as_view(), name='create_book'),
    path('up', views.UserPreferenceView.as_view(), name='up'),
    path('add', views.playlist, name='add'),

]

urlpatterns += staticfiles_urlpatterns()
