import spotipy
import json
import pprint
import csv
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

cid ="2a7c83df560d4c16826dbea523952b12" 
secret = "5e4aebcf15a9467d9618c2b040df49ab" 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False
index = 1
df = pd.DataFrame()
with open('billboards.csv') as data:
    reader = csv.DictReader(data)
    for row in reader:
        print index
        trackName = row['Song']
        artistName = row['Artist']
        try:
            results = sp.search(q = "track:" + trackName + " " + "artist:" + artistName, type = "track")
            tracks = results["tracks"]["items"][0]["id"]
            ids = [tracks]
            feature = sp.audio_features(ids)
            df = df.append(feature, ignore_index=True)
        except IndexError:        
            print 'InvalidSearch!'
            df.loc[len(df)] = 'NULL' 
        index += 1
df.to_csv('out.csv')
