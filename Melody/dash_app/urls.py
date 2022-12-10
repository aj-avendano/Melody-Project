from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "dash_app"

urlpatterns = [
    path("", views.homepage.as_view(), name="homepage"),
    path("register", views.RegisterRequest.as_view(), name="register"),#kuldeep
    path('login', views.LoginRequest.as_view(), name='login'),#kuldeep
    path('logout', views.LogoutRequest.as_view(), name='logout'),#kuldeep
    path('dashboardHome', views.dashboardHome.as_view(), name="dashboardHome"),#kuldeep
    path('generator', views.generator.as_view(), name="generator"),#Jaimit
    path('add_item', views.PlaylistItemView.as_view(), name='add_item'),#Anthony
    path('item', views.PlaylistItemsCreateView.as_view(), name='item'),#Anthony
    path('create_playlist', views.PlayListCreateView.as_view(), name='create_playlist'),#Anthony
    path('display_playlist', views.DisplayPlaylistView.as_view(), name='display_playlist'),#kuldeep
    path('UserPreferences', views.UserPreferenceView.as_view(), name='UserPreferences'),#Anthony
    path('search_results_genre', views.SearchGenre.as_view(), name="search_results_genre"),#Jason
    path('search_results_artist', views.SearchArtist.as_view(), name="search_results_artist"),#Jaimit
    path('search_results_song', views.SearchSong.as_view(), name="search_results_song"),#Jason
    path('search_results_album', views.SearchAlbum.as_view(), name="search_results_album"),#Jaimit
    path('search_genre_artist', views.SearchArtistsInGenre.as_view(), name="search_genre_artist"),#Jason
]

urlpatterns += staticfiles_urlpatterns()
