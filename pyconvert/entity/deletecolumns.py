import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../../data/test.csv')
df = df[['id','acousticness','danceability','duration_ms','energy','instrumentalness','liveness','loudness','speechiness','tempo','valence', 'Song', 'Year']]
print(df)
#df = df.rename(columns={'album_id': 'id', 'album_name':'name', 'album_type':'type'})
df.to_csv('songAttributes.csv', index=False, encoding='utf-8', header=False)
