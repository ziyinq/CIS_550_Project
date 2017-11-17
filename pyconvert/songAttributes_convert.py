import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../data/songAttributes.csv')
df = df[['id','acousticness','danceability','duration_ms','energy','instrumentalness','key','liveness','loudness','mode','speechiness','tempo','time_signature','valence']]
#df = df.rename(columns={'album_id': 'id', 'album_name':'name', 'album_type':'type'})
df.to_csv('songAttributes_converted.csv', index=False, encoding='utf-8', header=True)
