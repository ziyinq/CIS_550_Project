import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../data/album.csv')
df = df[['album_id','artist_id']]
df.to_csv('in.csv', index=False, encoding='utf-8', header=False)
