import pandas as pd

df = pd.DataFrame()
df = pd.read_csv('../data/belong.csv')
belong = pd.DataFrame()
i = 0
for index,row in df.iterrows():
    artist_id = row['artist_id']
    try:
        for genre in row['genres'].split(","):
            genre = genre.strip("[").strip("]").strip()
            data = {}
            data["artist_id"] = "\"" + artist_id + "\""
            data["genre"] = "\"" + genre + "\""
            belong = belong.append(data, ignore_index = True)
    except AttributeError:
        data = {}
        try:
            data["artist_id"] = "\"" + artist_id + "\""
        except TypeError:
            data["artist_id"] = artist_id
        data["genre"] = genre
        belong = belong.append(data, ignore_index = True)
belong.to_csv('belong.csv', index=False, encoding='utf-8', header=False)
