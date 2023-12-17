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

    # Get Spotify API credentials from environment variables #TODO: Wrong
    SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']

    # Create a SpotifyOAuth object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                            client_secret=SPOTIPY_CLIENT_SECRET,
                                                 scope='playlist-read-private'))

    # Extract playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1]

    # Get the tracks from the playlist
    results = sp.playlist_tracks(playlist_id)

    # Print information about each track
    for track in results['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        print(f"Track: {track_name} - Artist: {artist_name}")


################################################################################
