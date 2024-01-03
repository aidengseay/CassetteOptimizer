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

## Demo

### Input
You will paste your appropriate Spotify playlist link in the command line (see [Input Specifications](https://github.com/aidengseay/CassetteOptimizer/blob/dev/README.md#input-specifications))

![Screenshot 2024-01-02 164126](https://github.com/aidengseay/CassetteOptimizer/assets/108606344/1cc72e85-b50a-4f23-b8bb-b9322e1e1f35)

### Output
The program will return a text file of all the songs you can fit onto the cassette. 

![Screenshot 2024-01-02 164220](https://github.com/aidengseay/CassetteOptimizer/assets/108606344/9c9f6320-fd61-4a7d-b90f-b316e4f34ce4)

## Input Specifications

A Python file will take data from Spotify via Spotipy API. The user must input a
playlist such as below:

https://open.spotify.com/playlist/37i9dQZF1DWSIXPHRZ4SKc

The program will take in the song title, artist, and song duration (sec).

## Optimization Specifications

This program will use the multiple knapsack problem. The implementation outline 
to solve this problem is below. 

Knapsack problem: https://developers.google.com/optimization/pack/multiple_knapsack
