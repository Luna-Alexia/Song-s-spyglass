import spotipy
import json
import requests
from spotipy.oauth2 import SpotifyClientCredentials
#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id="Enter CLient ID here", client_secret="Enter Secret here")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

class Song():
    def __init__(self, song) -> None:
        self.playlist_link = song
        self.playlist_URI = self.playlist_link.split("/")[-1].split("?")[0]
        self.track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(self.playlist_URI)["items"]]
        

   
    def Luna(self):
        counter = 1
        bar = "-"
        varMaxList = len(self.track_uris)
        with open("Songs.txt", "w", encoding="utf8") as f:
            for track in sp.playlist_tracks(self.playlist_URI)["items"]:
            #print(f"TESTING --- {track}")
            #URI
                track_uri = track["track"]["uri"]
                #print(track_uri)

            #Track name
                track_name = track["track"]["name"]
            #self.songList.append(track_name)
            
            #Main Artist
                artist_uri = track["track"]["artists"][0]["uri"]
                artist_info = sp.artist(artist_uri)
    
            #Name, popularity, genre
                artist_name = track["track"]["artists"][0]["name"]
                artist_pop = artist_info["popularity"]
                artist_genres = artist_info["genres"]
            #self.songGenreList.append(artist_genres)

            #Album
                album = track["track"]["album"]["name"]
            
            
            #Popularity of the track
                track_pop = track["track"]["popularity"]


                #f.write(str(counter) + ") "+ "Album: "+ album + ", Song: "+ track_name + ", Genres:"+ " [" +" | ".join(artist_genres)+ "]"+ ", Popularity: " +str(track_pop) + '\n')
                f.write(str(counter) + ") "+"Song: "+ track_name + "\nGenres:"+ " [" +" | ".join(artist_genres) +"]" +'\n\n')

                print(f"Loading: {counter}/{varMaxList}")

                bar += "-"
                counter += 1
                
            
        f.close()