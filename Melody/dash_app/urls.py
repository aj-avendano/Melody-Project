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
    #path('dashboard', views.dashboard, name="dashboard"),
    path('dashboardHome', views.dashboardHome, name="dashboardHome"),
    path('preferences', views.preferences, name="preferences"),
    path('generator', views.generator, name="generator"),
    path('create_playlist', views.PlayListCreateView.as_view(), name='create_playlist'),
    path('UserPreferences', views.UserPreferenceView.as_view(), name='UserPreferences'),
    path('search_results_genre', views.SearchGenre.as_view(), name="search_results_genre"),
    path('search_results_artist', views.SearchArtist.as_view(), name="search_results_artist"),
    path('search_results_song', views.SearchSong.as_view(), name="search_results_song"),
    path('search_results_album', views.SearchAlbum.as_view(), name="search_results_album"),
    # path('search', views.SearchGenre.as_view(), name="search_results"),
    path('search_genre_artist', views.SearchArtistsInGenre.as_view(), name="search_genre_artist"),
]

urlpatterns += staticfiles_urlpatterns()
