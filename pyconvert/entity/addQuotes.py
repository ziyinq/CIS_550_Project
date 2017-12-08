import pandas as pd

relIn = pd.DataFrame()
df = pd.DataFrame()
df = pd.read_csv('../../data_convert/entity/songAttributes_header.csv')

for index,row in df.iterrows():
    data = {}
    try:
        myid = "\"" + row["id"] + "\""
    except TypeError:
        myid = row["id"]
    try:
        acousticness = "\"" + row["acousticness"] + "\""
    except TypeError:
        acousticness = row["acousticness"]
    try:
        danceability = "\"" + row["danceability"] + "\""
    except TypeError:
        danceability = row["danceability"]
    try:
        duration_ms = "\"" + row["duration_ms"] + "\""
    except TypeError:
        duration_ms = row["duration_ms"]
    try:
        energy = "\"" + row["energy"] + "\""
    except TypeError:
        energy = row["energy"]
    try:
        instrumentalness = "\"" + row["instrumentalness"] + "\""
    except TypeError:
        instrumentalness= row["instrumentalness"]
    try:
        key = "\"" + row["key"] + "\""
    except TypeError:
        key= row["key"]
    try:
        liveness = "\"" + row["liveness"] + "\""
    except TypeError:
        liveness= row["liveness"]
    try:
        loudness = "\"" + row["loudness"] + "\""
    except TypeError:
        loudness= row["loudness"]
    try:
        mode = "\"" + row["mode"] + "\""
    except TypeError:
        mode= row["mode"]
    try:
        speechiness = "\"" + row["speechiness"] + "\""
    except TypeError:
        speechiness= row["speechiness"]
    try:
        tempo = "\"" + row["tempo"] + "\""
    except TypeError:
        tempo= row["tempo"]
    try:
        time_signature = "\"" + row["time_signature"] + "\""
    except TypeError:
        time_signature= row["time_signature"]
    try:
        valence = "\"" + row["valence"] + "\""
    except TypeError:
        valence= row["valence"]
    try:
        Song = "\"" + row["Song"] + "\""
    except TypeError:
        Song= row["Song"]
    try:
        Year = "\"" + row["Year"] + "\""
    except TypeError:
        Year= row["Year"]

    data["id"] = myid
    data["acousticness"] = acousticness
    data["danceability"] = danceability
    data["duration_ms"] = duration_ms
    data["energy"] = energy
    data["instrumentalness"] = instrumentalness
    data["key"] = key
    data["liveness"] = liveness
    data["loudness"] = loudness
    data["mode"] = mode
    data["speechiness"] = speechiness
    data["tempo"] = tempo
    data["time_signature"] = time_signature
    data["valence"] = valence
    data["Song"] = Song
    data["Year"] = Year
    relIn = relIn.append(data, ignore_index = True)
relIn.to_csv('test.csv', index=False, encoding='utf-8', header=True)
