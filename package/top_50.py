import requests
from spotify import authenticate

# Spotify global top 50 playlist: https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF


def get_top_50_links():

    # Get an authentication token
    token = authenticate()

    # Add authentication token to the request headers
    headers = {
        'Authorization': 'Bearer {token}'.format(token=token)
    }

    query_url = 'https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF'

    # Query the Spotify API for the song
    response = requests.get(query_url, headers=headers)
    # Parse the response into a dictionary (JSON)
    response = response.json()

    # print(response)
    # print(len(response))
    # print(response.keys())
    # print(response['tracks'])
    # print(len(response['tracks']))
    # print(response['tracks'].keys())
    # print(response['tracks']['items'])
    # print(response['tracks']['items'][0]['track']['external_urls']['spotify'])

    song_links = [song['track']['external_urls']['spotify']
                  for song in response['tracks']['items']]

    # print([song['uri'] for song in response['tracks']['items']])

    # song_links = [track for track in response['tracks']]

    print(song_links)
    print(len(song_links))


if __name__ == '__main__':
    get_top_50_links()
