import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

def list_lists(inn):
    while inn.lstrip().rstrip().lower() == 'list':
        print('###############################\nPlaylist list:')
        for index, result in enumerate(lists):
            print(index + 1, result)
        inn = input(
            '###############################\nIf you would like to see the list repeated, please type \'list\', '
            'otherwise type in the name of the playlist that you would like to view songs from.\n')
    return inn


scope = 'playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlists = sp.current_user_playlists(limit=50)
lists = set()
id_map = {}
for result in playlists['items']:
    lists.add(result['name'])
    id_map[result['name']] = result['id']
inn = input('Please input the name of the playlist that you would like to view songs from. If you\'re unsure of '
            'which playlists are available, please type \'list\'.\n')
while inn.lstrip().rstrip().lower() != 'done':
    if inn.lstrip().rstrip().lower() == 'list':
        inn = list_lists(inn)
    elif inn in lists:
        items = sp.playlist_items(id_map[inn], limit=10, market='US')
        for index, item in enumerate(items['items']):
            print(index+1, item['track']['artists'][0]['name'], '-', item['track']['name'])
        inn = input('If you would like to view another playlist, just input its name, or type \'list\' to see all '
                    'avaliable playlists to view. If done, type \'done\' to quit program.\n')
    else:
        inn = input(f'{inn} is not part of the available list of playlists. Please input a valid list. To see all '
                    f'valid lists, please type \'list\'.\n')
