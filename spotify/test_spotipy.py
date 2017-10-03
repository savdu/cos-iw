import spotipy
spotify = spotipy.Spotify()
name = "Birdy"
results = spotify.search(q='artist:' + name, type='artist')
print results