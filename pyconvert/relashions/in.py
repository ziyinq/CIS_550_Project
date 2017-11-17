import pandas as pd

relIn = pd.DataFrame()
df = pd.DataFrame()
df2 = pd.DataFrame()
df = pd.read_csv('../data/album.csv')
df2 = pd.read_csv('../data/songAttributes.csv')
df = df[['album_id']]
df2 = df2[['id']]
df2 = df2.rename(columns={'id': 'song_id'})
df = pd.concat([df2,df],axis=1)
for index,row in df.iterrows():
    data = {}
    try:
        album_id = "\"" + row["album_id"] + "\""
    except TypeError:
        album_id = row["album_id"]
    try:
        song_id = "\"" + row["song_id"] + "\""
    except TypeError:
        song_id = row["song_id"]
    data["album_id"] = album_id
    data["song_id"] = song_id
    relIn = relIn.append(data, ignore_index = True)
relIn.to_csv('in.csv', index=False, encoding='utf-8', header=True)
