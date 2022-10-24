from lyricsgenius import Genius

genius = Genius("7EMFG8mbuXbGk62XG1W75EaAPd1DZtbPPjMzbGNryZ0YVzmgUCbjy6A9EGGi4o9A")
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
