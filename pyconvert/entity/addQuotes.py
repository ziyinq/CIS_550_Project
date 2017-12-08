import pandas as pd

relIn = pd.DataFrame()
df = pd.DataFrame()
df = pd.read_csv('../../data_convert/entity/songAttributes_header.csv')

for index,row in df.iterrows():
    data = {}
    myid = row["id"]
    Song = row["Song"]
    try:
        acousticness = "\"" + str(row["acousticness"]) + "\""
    except TypeError:
        acousticness = str(row["acousticness"])
    try:
        danceability = "\"" + str(row["danceability"]) + "\""
    except TypeError:
        danceability = str(row["danceability"])
    try:
        duration_ms = "\"" + str(row["duration_ms"]) + "\""
    except TypeError:
        duration_ms = str(row["duration_ms"])
    try:
        energy = "\"" + str(row["energy"]) + "\""
    except TypeError:
        energy = str(row["energy"])
    try:
        instrumentalness = "\"" + str(row["instrumentalness"]) + "\""
    except TypeError:
        instrumentalness= str(row["instrumentalness"])
    try:
        key = "\"" + str(row["key"]) + "\""
    except TypeError:
        key= str(row["key"])
    try:
        liveness = "\"" + str(row["liveness"]) + "\""
    except TypeError:
        liveness= str(row["liveness"])
    try:
        loudness = "\"" + str(row["loudness"]) + "\""
    except TypeError:
        loudness= str(row["loudness"])
    try:
        mode = "\"" + str(row["mode"]) + "\""
    except TypeError:
        mode= str(row["mode"])
    try:
        speechiness = "\"" + str(row["speechiness"]) + "\""
    except TypeError:
        speechiness= str(row["speechiness"])
    try:
        tempo = "\"" + str(row["tempo"]) + "\""
    except TypeError:
        tempo= str(row["tempo"])
    try:
        time_signature = "\"" + str(row["time_signature"]) + "\""
    except TypeError:
        time_signature= str(row["time_signature"])
    try:
        valence = "\"" + str(row["valence"]) + "\""
    except TypeError:
        valence= str(row["valence"])
    try:
        Year = "\"" + str(row["Year"]) + "\""
    except TypeError:
        Year= str(row["Year"])

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
