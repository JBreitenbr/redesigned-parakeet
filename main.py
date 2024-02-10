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
import spotipy
import spotipy.util as util
from os import listdir
import pandas as pd

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


d=pd.read_csv('streamingHistory_1.csv')
def get_api_id(track_name,artist):
   
    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer '+ 'BQD2CL0He4PiSVl7YGGBrXP_oteJHJ705F0dzohMYkCIwoczfpgY1mxDxT6UeIxiOYiqtcwn6haFhk7kqxV0PifZzuRoZmcRj5snq0b647YQ_9gH-qqoM9cbWGGRkaUgZ_LZRnVyn0U3Wmd5OJQbFGXIlxQX5oCyum_J5-6QdgjUqpBDj31fXDjXxKV4ejARH5EmHoRbxe8baaPNTJGl6agidU9DlXVpS6qtewwSQTBwIdq47KMtKsov49MUPgadSd5kSTkVBY83conFORc1Uz8bJo2T'

  }
    params = [
    ('q', track_name),
    ('type', 'track'),
    ]
    
    if artist: 
        params.append(('artist', artist))
        
    try:
        response = requests.get('https://api.spotify.com/v1/search', 
                    headers = headers, params = params, timeout = 5)
        json = response.json()
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except:
        return None
df_dic1={}
for i in range(4300,4841):
   tr_=get_api_id(d.iloc[i]["trackName"],d.iloc[i]["artistName"])
   fs=sp.audio_features(tracks=[tr_])
   df=pd.DataFrame.from_dict(fs)
   df["track"]=d.iloc[i]["trackName"]
   df["artist"]=d.iloc[i]["artistName"]
   df["msPlayed"]=d.iloc[i]["msPlayed"]
   df['datetime'] =   datetime.strptime(d.iloc[i]['endTime'], '%Y-%m-%d %H:%M')    
   df_dic1[i]=df
df_list=[]
for i in range(4300,4841):
  df_list.append(df_dic1[i])

whole=pd.concat(df_list)
whole.to_csv("batch8.csv")