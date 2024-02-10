from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

client_id = "dec967d105634e55942f249a600780f1"
client_secret = "33524391083f4259a50bb489370a48a6"
username = "31nfsp7vapk4zh24xzvw3lkavx5e"
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-recently-played'
import requests
from datetime import datetime
from typing import List
import spotipy.util as util
from os import listdir

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
lst1=[] # image url
lst2=[] # album id
lst3=[] # track id
df0=pd.read_csv("song_fundus.csv").iloc[800:1000]
print(len(df0))

for i in range(800,1000):
    artist=df0.loc[i,"artist"]
    track=df0.loc[i,"track"]
    track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track',limit=1)
    if track_id["tracks"]["items"]!=[]:
       trackId = track_id['tracks']['items'][0]
       lst1.append(trackId["album"]["images"][2]["url"])
       lst2.append(trackId["album"]["id"])
       lst3.append(trackId["id"])
    else:
      lst1.append("x")
      lst2.append("x")
      lst3.append("x")
df0["imgUrl"]=lst1
df0["album_id"]=lst2
df0["track_id"]=lst3
fauls=[]
for i in range(800,1000):
  if df0.loc[i,"imgUrl"]=="x":
    fauls.append(i)
print(fauls)
df0=df0.drop(fauls)
df0[["track_id","artist","track","album_id","imgUrl"]].to_csv("cleaned_1000.csv",index=False)



