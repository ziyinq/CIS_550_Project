import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../../data/song.csv')
df = df[['Song','id']]
df = df.dropna()
#print(df)
#df = df.rename(columns={'album_id': 'id', 'album_name':'name', 'album_type':'type'})
df.to_csv('songName.csv', index=False, encoding='utf-8', header=False)
