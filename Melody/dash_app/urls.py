from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "dash_app"

##Function Written by Jason Eissayou and Kuldeep and Joaquin
urlpatterns = [
    path("", views.homepage.as_view(), name="homepage"),
    path("register", views.RegisterRequest.as_view(), name="register"),
    path('login', views.LoginRequest.as_view(), name='login'),
    path('logout', views.LogoutRequest.as_view(), name='logout'),
    path('dashboardHome', views.dashboardHome.as_view(), name="dashboardHome"),
    path('generator', views.generator.as_view(), name="generator"),
    path('add_item', views.PlaylistItemView.as_view(), name='add_item'),
    path('item', views.PlaylistItemsCreateView.as_view(), name='item'),
    path('create_playlist', views.PlayListCreateView.as_view(), name='create_playlist'),
    path('display_playlist', views.DisplayPlaylistView.as_view(), name='display_playlist'),
    path('UserPreferences', views.UserPreferenceView.as_view(), name='UserPreferences'),
    path('search_results_genre', views.SearchGenre.as_view(), name="search_results_genre"),
    path('search_results_artist', views.SearchArtist.as_view(), name="search_results_artist"),
    path('search_results_song', views.SearchSong.as_view(), name="search_results_song"),
    path('search_results_album', views.SearchAlbum.as_view(), name="search_results_album"),
    path('search_genre_artist', views.SearchArtistsInGenre.as_view(), name="search_genre_artist"),
]

urlpatterns += staticfiles_urlpatterns()
