################################################################################
# Cassette Script Utility
# ========================
# This program takes in a list of songs and optimizes the best order to fit on a
# cassette. 
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
    playlistURL = input("Input Playlist URL: ")
    songInputList = CassetteInputUtility.getSongList(playlistURL)

    if songInputList == None:
        return 0
    
    # songInputList is ready for algo









################################################################################
main()
