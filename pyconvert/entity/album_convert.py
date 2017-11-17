import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../data/album.csv')
df = df[['album_id','album_name','album_type','releasedate','popularity']]
for index,row in df.iterrows():
    data = {}
    try:
        album_id = "\"" + row["album_id"] + "\""
    except TypeError:
        album_id = row["album_id"]
    try:
        album_name = "\"" + row["album_name"] + "\""
    except TypeError:
        album_name = row["album_name"]
    try:
        album_type = "\"" + row["album_type"] + "\""
    except TypeError:
        album_type = row["album_type"]
    try:
        releasedate = "\"" + row["releasedate"] + "\""
    except TypeError:
        releasedate = row["releasedate"]
    try:
        popularity = "\"" + row["popularity"] + "\""
    except TypeError:
        popularity = row["popularity"]
    data["album_id"] = album_id
    data["artist_id"] = artist_id
    artist = artist.append(data, ignore_index = True)
df.to_csv('album.csv', index=False, encoding='utf-8', header=True)
