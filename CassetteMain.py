################################################################################
# Cassette Main
# =============
# This program takes in a list of songs and optimizes the best order to fit on a
# cassette. Main file.
# Created by Aiden Seay, Winter 2023
################################################################################
# IMPORTS
import CassetteInputUtility

################################################################################
# CONSTANTS

################################################################################

# Main 
def main():

    # Get the song input list
    playlistURL = "https://open.spotify.com/playlist/0DzTpmJhUZNdmWvWhYf2ME"
    print("Input Playlist URL: https://open.spotify.com/playlist/0DzTpmJhUZNdmWvWhYf2ME")
    
    songInputList = CassetteInputUtility.getSongList(playlistURL)

    if songInputList == None:
        return 0
    
    print(songInputList)








################################################################################
main()
