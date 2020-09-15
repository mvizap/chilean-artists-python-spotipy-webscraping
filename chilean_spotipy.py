import spotipy
from spotipy import SpotifyClientCredentials, util
import time
from IPython.core.display import clear_output
import pandas as pd


#Credentials to access the Spotify Music Data
client_id='your-client-id'
client_secret='your-secret-id'
redirect_uri='http://127.0.0.1:9090'
username = 'your-username'
scope = 'your-scope'

auth_manager = spotipy.oauth2.SpotifyOAuth(username=username,
                                            scope=scope,
                                            client_id=client_id,
                                            client_secret=client_secret,
                                            redirect_uri=redirect_uri)
                                            
sp = spotipy.Spotify(auth_manager=auth_manager, requests_timeout=10)



def get_id_artist(name):
    results = []
    results = sp.search(q='artist:' + name, type='artist', market='CL')
    if len(results['artists']['items']) > 0:
        for result in results['artists']['items']:
            id = result['id']
            name_search = result['name']
            if name.lower() == name_search.lower():
                return id

def get_albums_id(ids):
    album_ids = []
    results = sp.artist_albums(ids)
    for album in results['items']:
        album_ids.append(album['id'])
    return album_ids

def get_album_songs_id(ids):
    song_ids = []
    results = sp.album_tracks(ids,offset=0)
    for songs in results['items']:
        song_ids.append(songs['id'])
    return song_ids
    
def get_songs_features(id):
    
    meta = sp.track(id)

    features = sp.audio_features(id)
    features.sort()

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']
    id =  meta['id']

    # features
    try:
        acousticness = features[0]['acousticness']
        danceability = features[0]['danceability']
        energy = features[0]['energy']
        instrumentalness = features[0]['instrumentalness']
        liveness = features[0]['liveness']
        valence = features[0]['valence']
        loudness = features[0]['loudness']
        speechiness = features[0]['speechiness']
        tempo = features[0]['tempo']
        key = features[0]['key']
        time_signature = features[0]['time_signature']
    except: 
        acousticness = danceability = energy = instrumentalness = 0
        liveness = valence = loudness = speechiness = tempo = key = time_signature = 0

    track = [name, album, artist, id, release_date, popularity, length, danceability, acousticness,
            energy, instrumentalness, liveness, valence, loudness, speechiness, tempo, key, time_signature]
    columns = ['name','album','artist','id','release_date','popularity','length','danceability','acousticness','energy','instrumentalness',
                'liveness','valence','loudness','speechiness','tempo','key','time_signature']
    return track,columns



def get_songs_artist_ids_playlist(ids):
    playlist = sp.playlist_tracks(ids)
    songs_id = []
    artists_id = []
    for result in playlist['items']:
        songs_id.append(result['track']['id'])
        for artist in result['track']['artists']:
            artists_id.append(artist['id'])
    return songs_id,artists_id

def download_albums(music_id,artist=False):

    if artist == True:
        ids_album = get_albums_id(music_id)
    else:
        if type(music_id) == list:
            ids_album = music_id
        elif type(music_id) == str:
            ids_album = list([music_id])

    tracks = []
    for ids in ids_album:
        #Obtener Ids de canciones en album
        song_ids = get_album_songs_id(ids=ids)
        #Obtener feautres de canciones en album
        #time.sleep(.6) 

        for song_id in song_ids:
            if song_id not in tracks:
                track, columns = get_songs_features(song_id)
                tracks.append(track)
        print(f"Artista:  {track[2]} - Album {track[1]}")
        clear_output()
        
    clear_output()
 
    return tracks,columns

def get_artists_in_spotify(artists):
    artists=[]
    artists = pd.read_csv('data/ws.csv')

    spotify_artists = []
    for artist in artists['nombre']:
        id_artist= get_id_artist(artist)
        if id_artist != None:
            spotify_artists.append(artist)
            return spotify_artists
    ws = pd.DataFrame(spotify_artists, columns=['name'])
    ws.to_csv('data/wsConfirm.csv',index=False)

def get_all_info(name, count, first, text = ' LEYENDO A '):
    id_artist= get_id_artist(artist)
    if id_artist != None:
        print(str(count) + text + artist)
        tracks,columns = download_albums(id_artist,artist=True)
        df1 = pd.DataFrame(tracks,columns=columns)
        if first == True:
            first = False
            df1.to_csv('data/ids4.csv', index=False)
        else: 
            df1.to_csv('data/ids4.csv', mode='a', header=False, index=False)


artists=[]
first = True
count = 0
artists = pd.read_csv('data/wsConfirm.csv')

for artist in artists['name']:
    try:
        count = count + 1
        get_all_info(artist, count, first)
    except spotipy.client.SpotifyException: 
        print("############ REFRESHING TOKEN #############")
        cached_token = auth_manager.get_cached_token()
        refreshed_token = cached_token['refresh_token']
        new_token = auth_manager.refresh_access_token(refreshed_token)
        sp = spotipy.Spotify(auth=new_token['access_token'])

        get_all_info(artist, count, first, ' LEYENDO NUEVAMENTE A ')
        
        

