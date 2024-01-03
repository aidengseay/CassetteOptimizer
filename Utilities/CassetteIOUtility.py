################################################################################
# Cassette IO Utility
# ======================
# This file is responsible for getting the proper input playlist from spotify.
# Created by Aiden Seay, Winter 2023
################################################################################
# IMPORTS
import os
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

################################################################################
# CLASSES
class Song:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

################################################################################
# CONSTANTS
OUTPUT_FILE = "cassette.txt"

################################################################################

def getSongList(playlist_url):

    # Get Spotify API credentials from environment variables
    SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

    try:
        # Create a SpotifyOAuth object
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                            client_id=SPOTIPY_CLIENT_ID,
                                            client_secret=SPOTIPY_CLIENT_SECRET,
                                            redirect_uri=SPOTIPY_REDIRECT_URI,
                                                 scope='playlist-read-private'))

        playlist_id = playlist_url.split('/')[-1]

        # Get the tracks from the playlist (max 100 songs)
        results = sp.playlist_tracks(playlist_id)

        returnList = []

        # Print information about each track
        for track in results['items']:
            trackName = track['track']['name']
            artistName = track['track']['artists'][0]['name']
            duration = track['track']['duration_ms'] // 1000 # unit: seconds

            returnList.append(Song(name=trackName, artist=artistName, 
                                                             duration=duration))

        return returnList
    
    except:
        return None
    
def returnSongList(cassetteSongList):

    with open(OUTPUT_FILE, "w") as outFile:

        outFile.write("Cassette Songs\n")
        outFile.write("==============\n\n")

        count = 0

        for side in cassetteSongList:

            if count == 0:
                outFile.write("Side A\n")
                count += 1
            else:
                outFile.write("Side B\n")

            outFile.write("------\n")

            for song in side:
                outFile.write(f"{song.name} -- [{song.artist}]\n")

            outFile.write(f"\n")



################################################################################
