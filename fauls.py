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

df0=pd.read_csv("song_fundus.csv")
fauls=[615,619,652,678,718,719,769,770,771,779,783,785,788,789]

for i in fauls:
  print(df0.loc[i,"artist"])
  print(df0.loc[i,"track"])