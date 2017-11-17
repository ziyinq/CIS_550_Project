import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../data/artists.csv')
#df = df['genres']
df = df[['artist_id','artist_name','followers','popularity']]
#df = df.rename(columns={'album_id': 'id', 'album_name':'name', 'album_type':'type'})
df.to_csv('artists.csv', index=False, encoding='utf-8', header=True)
