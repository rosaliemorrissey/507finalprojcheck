# Documentation to Create Playlist on Spotify
import spotifyrequest
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import requests
import json
import requests_cache
import api_info


requests_cache.install_cache('spotify_cache', expire_after=86400)


AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': api_info.client_id,
    'client_secret': api_info.client_secret
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON file and converts it to a Python dictionary.

    Parameters:
        filepath (str): a path to the JSON  
        file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


# ARTIST IDS
taylor_swift = "spotify:artist:06HL4z0CvFAxyc27GXpf02"
muna = "spotify:artist:6xdRb2GypJ7DqnWAI2mHGn"
paramore = "spotify:artist:74XFHRwlV6OrjEM0A2NCMF"
gayle = "spotify:artist:2VSHKHBTiXWplO8lxcnUC9"
beabadoobee = "spotify:artist:35l9BRT7MXmM8bv2WDQiyB"
gracie_abrams = "spotify:artist:4tuJ0bMpJh08umKkEXKUI5"
phoebe_bridgers = "spotify:artist:1r1uxoy19fzMxunt3ONAkG"
owenn = "spotify:artist:3OBSOHlmPjy77DRRrRubFs"
girl_in_red = "spotify:artist:3uwAm6vQy7kWPS2bciKWx9"
haim = "spotify:artist:4Ui2kfOqGujY81UcPrb5KE"


eras_tour = read_json('ErasTourDict.json')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


def get_album_data(artist_id):
    """takes artist id and finds all albums from the spotify API
    PARAMS:
    artist_id(str): unique id for the artist from the API
    returns
    albums(dict): details for all albums by artist"""
    results = spotify.artist_albums(artist_id=artist_id, country='US')
    albums = results["items"]
    while results['next']:
        # albums.extend(results['items'])

        # for album in albums:
        #     del album["available_markets"]
        # del album["album_group"]
        # del album["album_type"]
        # del album["images"]
        # del album["release_date_precision"]
        # del album["total_tracks"]
        # del album["type"]
        # del album["release_date"]
        # del album["external_urls"]
        return albums

taylor_album = get_album_data(taylor_swift)

def get_track_data(albums):
    """takes dict of album data and requests all tracks on the album from api
    PARAMS:
    albums(dict): contains albums and theur spotify ID
    RETURNS:
    list: all tracks and their spotify id"""
    tracks = []
    for album in albums:
        results = spotify.album_tracks(album_id=album["uri"], market="US")
        tracks.append(results['items'])
    return tracks

# taylor_tracks = get_track_data(taylor_album)


def get_audio_features(tracks):
    """requests spotify audio features (such as dancability, acousticness, energy, etc.)
    from the track's unique ID.
    PARAMS:
    tracks(list): tracks with unique ID
    RETURNS
    tracks(list): with added dict of audio features"""
    for track in tracks:
        for detail in track:
            detail["audio_features"] = spotify.audio_features(tracks=detail['uri'])
    return tracks

# taylor_audio_features = get_audio_features(taylor_tracks)
# print(taylor_audio_features)

def request_spotify_data(artist_id):
    """uses other functions to get all spotify information from api
     PARAMS:
      artist_id(str): unique id for the artist
    RETURNS:
     JSON of all collected data """
    albums = get_album_data(artist_id)
    tracks = get_track_data(albums)
    songs = get_audio_features(tracks)
    return songs


taylor_data = request_spotify_data(taylor_swift)
write_json("taylor_swift_data.json", taylor_data)

muna_data = request_spotify_data(muna)
# print(muna_data)
write_json("muna_data.json", muna_data)

paramore_data = request_spotify_data(paramore)
# print(paramore_data)
write_json("paramore_data.json", paramore_data)

gayle_data = request_spotify_data(gayle)
write_json("gayle_data.json", gayle_data)

beabadoobee_data = request_spotify_data(beabadoobee)
write_json("beabadoobee_data.json", beabadoobee_data)

gracie_abrams_data = request_spotify_data(gracie_abrams)
write_json("gracie_abrams_data.json", gracie_abrams_data)

phoebe_bridgers_data = request_spotify_data(phoebe_bridgers)
write_json("phoebe_bridgers_data.json", phoebe_bridgers_data)

# owenn_data = request_spotify_data(owenn)
# write_json("owenn_data.json", owenn_data)

girl_in_red_data = request_spotify_data(girl_in_red)
write_json("girl_in_red_data.json", girl_in_red_data)

haim_data = request_spotify_data(haim)
write_json("haim_data.json", haim_data)


owenn_results = spotify.artist_albums(owenn, country="US")
owenn_albums = owenn_results['items']
owenn_data =[]
for album in owenn_albums:
    owenn_results = spotify.album_tracks(album_id=album["uri"], market="US")
    owenn_data.append(owenn_results['items'])


for track in owenn_data:
    for detail in track:
        detail["audio_features"] = spotify.audio_features(tracks=detail["uri"])

write_json("owenn_data.json", owenn_data)

# user_id = input("What is your spotify user name? \n")


concert = input("What date are you seeing the Eras Tour? \n Provide the date as Month 00, 2023 such as April 23, 2023 or June 2, 2023.\n")

for date in eras_tour:
    if date == concert:
        # print (date["openers"])
            # openers = detail["openers"]
            # print(openers)
    # else:
    #     concert = input("Sorry! Nothing matched the date you entered. Please enter the date in the format 'Month 00, 2023 examples: April 23, 2023 or April 3, 2023")
