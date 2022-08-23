from fileinput import filename
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pytube import Search
from pytube import YouTube
from pytube import Stream

from VARIABLES import CLIENT_ID, CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DXbbu94YBG7Ye"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
playlistName = sp.playlist(playlist_URI)["name"]
songsDownloaded = 0

for i in range(1):
    for track in sp.playlist_tracks(playlist_URI, offset=i*100, limit=100)["items"]:
        # URI
        track_uri = track["track"]["uri"]
        # Track name
        track_name = track["track"]["name"]
        # Main Artist
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)
        #Name, popularity, genre
        artist_name = track["track"]["artists"][0]["name"]
        # Album
        album = track["track"]["album"]["name"]
        songsDownloaded += 1
        songName = f"{track_name} - {artist_name}"
        # Armo el nombre de la cancion
        print(songName)
        downloadSongName = f"{songName}.mp4"
        # Agarro el primer resultado de la busqueda
        songResults = Search(songName).results[0]
        OUTPUT_PATH = f"E:\Programming\Python & Data Science & Machine learning\{playlistName}"
        # Agarro el ultimo resultado de la lista, ya que es el que tiene mejor definicion y es solo audio.
        songResults.streams.filter(only_audio=True, subtype="mp4")[-1].download(
            output_path=OUTPUT_PATH, filename=downloadSongName)

print(f"Songs downloaded: {songsDownloaded}")
