# Documentation to Create Playlist on Spotify
import spotifyrequest
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import requests
import json
import requests_cache


requests_cache.install_cache('spotify_data_cache', expire_after=86400)
client_id = "2fae25b923dd4125b3c95b6bcc1a7b6c"
client_secret = "96abf70264034a459250f12ab9438fbb"

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
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

# ARTIST IDS
taylor_swift = "spotify:artist:06HL4z0CvFAxyc27GXpf02"
muna = "6xdRb2GypJ7DqnWAI2mHGn"
paramore = "74XFHRwlV6OrjEM0A2NCMF"
gayle = "2VSHKHBTiXWplO8lxcnUC9"
beabadoobee = "35l9BRT7MXmM8bv2WDQiyB"
gracie_abrams = "4tuJ0bMpJh08umKkEXKUI5"
phoebe_bridgers = "1r1uxoy19fzMxunt3ONAkG"
owenn = "3OBSOHlmPjy77DRRrRubFs"
girl_in_red = "3uwAm6vQy7kWPS2bciKWx9"
haim = "4Ui2kfOqGujY81UcPrb5KE"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


def get_album_data(artist_id):
    """takes artist id and finds all albums from the spotify API
    PARAMS:
    artist_id(str): unique id for the artist from the API
    returns
    albums(dict): details for all albums by artist"""
    results = spotify.artist_albums(artist_id=artist_id, album_type="album", country='US')
    albums = results["items"]
    while results['next']:
        albums.extend(results['items'])

        # for album in albums:
        #     del album["album_type"]
        #     del album["images"]
        #     del album["release_date_precision"]
        #     del album["total_tracks"]
        #     del album["type"]
        #     del album["release_date"]
        #     del album["external_urls"]
    return albums


def get_track_data(albums):
    """takes dict of album data and requests all tracks on the album from spotify
    api.
    PARAMS:
    ALBUMS(dict): contains albums by artist and they spotify id
    RETURNS
    LIST: of all tracks and their spotify id"""
    tracks = []
    for album in albums:
        results = spotify.album_tracks(album_id=album['uri'], market="US")
        tracks.append(results['items'])
        for track in tracks:
            for detail in track:
                del detail['disc_number']
                del detail["duration_ms"]
                del detail['explicit']
                del detail['external_urls']
                del detail['is_local']
                del detail['is_playable']
                del detail['preview_url']
                del detail['track_number']
                del detail['type']
    return tracks


def get_audio_features(tracks):
    """requests spotify audio features (such as danceability, acousticness, energy, etc.)
    from the track's unique id
    PARAMS:
    tracks(list): tracks with unique id
    RETURNS
    tracks(list): with added dict of audio features"""
    for track in tracks:
        for detail in track:
            detail["audio_features"] = spotify.audio_features(tracks=detail['uri'])
    return tracks

taylor_swift_data = get_album_data(taylor_swift)
write_json('taylor_swift_data.json', taylor_swift_data)