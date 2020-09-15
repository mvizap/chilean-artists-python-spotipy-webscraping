import pandas as pd
import os

songs = []
songs = pd.read_csv('data/ids4.csv')

#print(songs.info())

name_artists = []
name_artists = pd.read_csv('data/wsConfirm.csv')

print(songs.shape[0])
songs = songs.drop_duplicates()
print(songs.shape[0])
songs['release_date'] = pd.to_datetime(songs['release_date'])

is_artist = songs[songs['artist'].isin(name_artists['name']) & songs['popularity'] > 0]



os.remove('data/ids4.csv')
is_artist.to_csv('data/ids4.csv', index=False)
