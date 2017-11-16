import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('data/artists.csv')
df = df['genres']
#df = df.rename(columns={'album_id': 'id', 'album_name':'name', 'album_type':'type'})
df.to_csv('genres.csv', encoding='utf-8', header=None, index=False)
