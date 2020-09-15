import pandas as pd

songs = []
songs = pd.read_csv('data/ids4.csv')

popular_old = songs[(songs['release_date'] >= '1900-01-01') & (songs['release_date'] < '1980-01-01')].sort_values('popularity',ascending=False).head(100)
popular_80 = songs[(songs['release_date'] >= '1980-01-01') & (songs['release_date'] < '1990-01-01')].sort_values('popularity',ascending=False).head(100)
popular_90 = songs[(songs['release_date'] >= '1990-01-01') & (songs['release_date'] < '2000-01-01')].sort_values('popularity',ascending=False).head(100)
popular_00 = songs[(songs['release_date'] >= '2000-01-01') & (songs['release_date'] < '2010-01-01')].sort_values('popularity',ascending=False).head(100)
popular_10 = songs[(songs['release_date'] >= '2010-01-01') & (songs['release_date'] < '2020-01-01')].sort_values('popularity',ascending=False).head(100)
popular_20 = songs[(songs['release_date'] >= '2020-01-01') & (songs['release_date'] < '2021-01-01')].sort_values('popularity',ascending=False).head(100)

popular_old.to_csv('data/popular_songs_old.csv', index=False)
popular_80.to_csv('data/popular_songs_80.csv', index=False)
popular_90.to_csv('data/popular_songs_90.csv', index=False)
popular_00.to_csv('data/popular_songs_00.csv', index=False)
popular_10.to_csv('data/popular_songs_10.csv', index=False)
popular_20.to_csv('data/popular_songs_20.csv', index=False)