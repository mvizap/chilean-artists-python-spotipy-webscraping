import spotipy
from spotipy import SpotifyClientCredentials, util
import pandas as pd


username = 'your-username'
scope_playlist = 'your-scope'
client_id='your-client-id'
client_secret='your-secret-id'
redirect_uri='http://127.0.0.1:9090'


#Credentials to access the Spotify Music Data
auth_manager = spotipy.oauth2.SpotifyOAuth(username=username,
                                            scope=scope_playlist,
                                            client_id=client_id,
                                            client_secret=client_secret,
                                            redirect_uri=redirect_uri)
                                            
sp_playlist = spotipy.Spotify(auth_manager=auth_manager, requests_timeout=10)


popular_songs_00 = pd.read_csv("data/popular_songs_00.csv")
popular_songs_10 = pd.read_csv("data/popular_songs_10.csv")
popular_songs_20 = pd.read_csv("data/popular_songs_20.csv")
popular_songs_80 = pd.read_csv("data/popular_songs_80.csv")
popular_songs_90 = pd.read_csv("data/popular_songs_90.csv")
popular_songs_old = pd.read_csv("data/popular_songs_old.csv")

ids_00 = popular_songs_00['id'].tolist()
ids_10 = popular_songs_10['id'].tolist()
ids_20 = popular_songs_20['id'].tolist()
ids_80 = popular_songs_80['id'].tolist()
ids_90 = popular_songs_90['id'].tolist()
ids_old = popular_songs_old['id'].tolist()

playlist_20 = sp_playlist.user_playlist_create(username,"TOP CHILE 2020", public=True, description="Canciones Populares del 2020. Esta playlist se creó siguiendo la popularidad de cada cancion chilena según la API de spotify.")
sp_playlist.user_playlist_add_tracks(username, playlist_20['id'], ids_20)

playlist_10 = sp_playlist.user_playlist_create(username,"TOP CHILE 2010-2019", public=True, description="Canciones Populares de la decada del 2010. Esta playlist se creó siguiendo la popularidad de cada cancion chilena según la API de spotify.")
sp_playlist.user_playlist_add_tracks(username, playlist_10['id'], ids_10)

playlist_00 = sp_playlist.user_playlist_create(username,"TOP CHILE 00's", public=True, description="Canciones Populares de la decada del 2000. Esta playlist se creó siguiendo la popularidad de cada cancion chilena según la API de spotify.")
sp_playlist.user_playlist_add_tracks(username, playlist_00['id'], ids_00) 

playlist_90 = sp_playlist.user_playlist_create(username,"TOP CHILE 90's", public=True, description="Canciones Populares de la decada de los 90. Esta playlist se creó siguiendo la popularidad de cada cancion chilena según la API de spotify.")
sp_playlist.user_playlist_add_tracks(username, playlist_90['id'], ids_90) 

playlist_80 = sp_playlist.user_playlist_create(username,"TOP CHILE 80's", public=True, description="Canciones Populares de la decada de los 80. Esta playlist se creó siguiendo la popularidad de cada cancion chilena según la API de spotify.")
sp_playlist.user_playlist_add_tracks(username, playlist_80['id'], ids_80) 

playlist_old = sp_playlist.user_playlist_create(username,"TOP CHILE 70's 60's 50's", public=True, description="Canciones Populares chilenas antiguas. Esta playlist se creó siguiendo la popularidad de cada cancion chilena según la API de spotify.")
sp_playlist.user_playlist_add_tracks(username, playlist_old['id'], ids_old) 






 


