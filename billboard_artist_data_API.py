# get list of Artist with top 100 songs in 4 music Genres using billboard API
import billboard
from lyricsgenius import Genius
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# billboard_record_list parameters are two strings rec_type is the type of record retrived from the billboard chart object
# options are artist, title, and 'rank'
#chartname is the specfic chart records are retived from
# the result is the specficified records from the selected chart inputed into a list

#genre charts to get artist names
#greatest-of-all-time-mainstream-rock-artists
#greatest-alternative-artists
#greatest-country-artists
#greatest-of-all-time-latin-artists
#greatest-of-all-time-pop-songs-artists
#greatest-r-b-hip-hop-artists
def billboard_record_list(rec_type,chartname):
    chart = billboard.ChartData(chartname)
    rec_list =[]
    for item in chart:
        if rec_type == 'artist':
            record=item.artist
        elif rec_type == 'title':
            record=item.title
        elif rec_type == 'rank':
            record=item.rank
        rec_list.append(record)
    return rec_list

genius = Genius("7EMFG8mbuXbGk62XG1W75EaAPd1DZtbPPjMzbGNryZ0YVzmgUCbjy6A9EGGi4o9A")
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None
