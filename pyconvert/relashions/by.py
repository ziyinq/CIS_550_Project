import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../data/album.csv')
df = df[['album_id','artist_id']]
artist = pd.DataFrame()
for index,row in df.iterrows():
    data = {}
    try:
        album_id = "\"" + row["album_id"] + "\""
    except TypeError:
        album_id = row["album_id"]
    try:
        artist_id = "\"" + row["artist_id"] + "\""
    except TypeError:
        artist_id = row["artist_id"]
    data["album_id"] = album_id
    data["artist_id"] = artist_id
    artist = artist.append(data, ignore_index = True)
artist.to_csv('artist_header.csv', index=False, encoding='utf-8', header=True)
