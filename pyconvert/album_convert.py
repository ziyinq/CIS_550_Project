import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../data/album.csv')
df = df[['album_id','album_name','album_type','releasedate','popularity']]
df.to_csv('album.csv', index=False, encoding='utf-8', header=True)
