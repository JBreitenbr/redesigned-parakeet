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

df0=pd.read_csv("song_fundus.csv")[["track","artist","id"]].iloc[8:10]
trid=df0["id"].tolist()
targDict={}
targDict2={}
lst=[]
lst2=[]
for num in trid:
  tracks=sp.tracks(tracks=[num])
  targDict[num]=tracks["tracks"][0]["album"]["images"][2]["url"]
  targDict2[num]=tracks["tracks"][0]["album"]["id"]
  lst.append(targDict[num])
  lst2.append(targDict2[num])
df0["album_id"]=lst2
df0["imgUrl"]=lst
df0.to_csv("sample.csv",index=False)
df0[["id","artist","track","album_id","imgUrl"]].to_csv("check.csv",index=False)





