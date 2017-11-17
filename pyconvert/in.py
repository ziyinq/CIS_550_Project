import pandas as pd

df = pd.DataFrame()
df2 = pd.DataFrame()
df = pd.read_csv('../data/album.csv')
df2 = pd.read_csv('../data/songAttributes.csv')
df = df[['album_id']]
df2 = df2[['id']]
df2 = df2.rename(columns={'id': 'song_id'})
df = pd.concat([df2,df],axis=1)
df.to_csv('in.csv', index=False, encoding='utf-8', header=False)
