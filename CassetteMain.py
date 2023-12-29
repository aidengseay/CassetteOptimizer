################################################################################
# Cassette Main
# =============
# This program takes in a list of songs and optimizes the best order to fit on a
# cassette. Main file.
# Created by Aiden Seay, Winter 2023
################################################################################
# IMPORTS
from Utilities.CassetteIOUtility import *
from Utilities.CassettePackUtility import *


################################################################################
# CONSTANTS
BIN_SIZE = 2695

################################################################################

# Main 
def main():

    # Get the song input list
    #playlistURL = input("Input Playlist URL: ")
    playlistURL = "https://open.spotify.com/playlist/37i9dQZF1EP6YuccBxUcC1"
    songInputList = getSongList(playlistURL)

    # Check for input failure
    if songInputList == None:

        print("Insert valid Spotify playlist link")
        return 0
    
    # Processing
    cassetteSongList = [[],[]]
    packCassette(songInputList, cassetteSongList, BIN_SIZE )

    # Output results
    print("\nResults stored in cassette.txt")

    returnSongList(cassetteSongList)

    input("Press enter to exit... ")

################################################################################
main()
