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
            album_id = results["tracks"]["items"][0]["album"]["id"]
            album = sp.album(album_id)

            album_filter = {}
            album_filter["album_id"] = album['id']
            album_filter["album_name"] = album['name']
            album_filter["album_type"] = album['album_type']
            album_filter["artist_id"] = album['artists'][0]['id']
            album_filter["artist_name"] = album['artists'][0]['name']
            album_filter["popularity"] = album['popularity']
            album_filter["releasedate"] = album['release_date']
            album_filter["uri"] = album['uri']

            df = df.append(album_filter, ignore_index=True)
        except IndexError:        
            print 'InvalidSearch!'
            df.loc[len(df)] = 'NULL' 
        index += 1
df.to_csv('album.csv', encoding = 'utf-8')
