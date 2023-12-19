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

################################################################################

# Main 
def main():

    # Get the song input list
    #playlistURL = input("Input Playlist URL: ")
    playlistURL = "https://open.spotify.com/playlist/0DzTpmJhUZNdmWvWhYf2ME"
    songInputList = getSongList(playlistURL)

    # Check for input failure
    if songInputList == None:

        print("Insert valid Spotify playlist link")
        return 0
    
    # Processing
    cassetteSongList = [[],[]]
    packCassette(songInputList, cassetteSongList)

    # Output results
    print("Results stored in cassette.txt")

    returnSongList(cassetteSongList)

    input("Press enter to exit... ")

################################################################################
main()
