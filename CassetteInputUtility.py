################################################################################
# Cassette Input Utility
# ========================
# This file is responsible for getting the proper input playlist from spotify.
# The program will optimize the best songs to fit on the cassette.
# Created by Aiden Seay, Winter 2023
# ##############################################################################
# IMPORTS
import os
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

################################################################################

def getSongList(playlist_url):

    # Get Spotify API credentials from environment variables
    SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

    # Create a SpotifyOAuth object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                            client_secret=SPOTIPY_CLIENT_SECRET,
                                            redirect_uri=SPOTIPY_REDIRECT_URI,
                                                 scope='playlist-read-private'))

    # Extract playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1]

    # Get the tracks from the playlist (max 100 songs)
    results = sp.playlist_tracks(playlist_id)

    # Print information about each track
    for track in results['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        duration_s = track['track']['duration_ms'] // 1000

        print(f"Track: {track_name} - Artist: {artist_name} - Duration: {duration_s}")


################################################################################
