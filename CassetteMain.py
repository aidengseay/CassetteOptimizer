################################################################################
# Cassette Main
# =============
# This program takes in a list of songs and optimizes the best order to fit on a
# cassette. Main file.
# Created by Aiden Seay, Winter 2023
################################################################################
# IMPORTS
import Utilities.CassetteIOUtility as CassetteIOUtility

################################################################################
# CONSTANTS

################################################################################

# Main 
def main():

    # Get the song input list
    #playlistURL = input("Input Playlist URL: ")
    playlistURL = "https://open.spotify.com/playlist/0DzTpmJhUZNdmWvWhYf2ME"
    songInputList = CassetteIOUtility.getSongList(playlistURL)

    # Check for input failure
    if songInputList == None:

        print("Insert valid Spotify Playlist link")
        return 0
    
    # Assume correct user input

    returnSongList = [[],[]]
    
    print(songInputList)








################################################################################
main()
