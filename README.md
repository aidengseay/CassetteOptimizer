# Cassette Optimizer

Created by Aiden Seay, Winter 2023

## Overview

This project is taking a Spotify playlist and optimizing the best fit for a cassette. Each cassette has 45 minutes of audio on each side. This program takes this into account and does appropriate calculations so the cassette can have the most songs possible.

## How to use

1. Include necessary environmental variables `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` in your local system.
2. Execute `pip install spotipy`.
3. Execute `pip install ortools`. 
4. Run `python CassetteMain.py` in your terminal.
5. Input a Spotify playlist URL.
6. The program returns a text file `cassette.txt` with optimal song order for cassette conversion.

## Input Specifications

A Python file will take data from Spotify via Spotipy API. The user must input a
playlist such as below:

https://open.spotify.com/playlist/37i9dQZF1DWSIXPHRZ4SKc

The program will take in the song title, artist, and song duration (sec).

## Optimization Specifications

This program will use the multiple knapsack problem. The implementation outline 
to solve this problem is below. 

Knapsack problem: https://developers.google.com/optimization/pack/multiple_knapsack
