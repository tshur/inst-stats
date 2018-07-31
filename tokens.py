import requests

from credentials import CLIENT_ID
from utils import check, pprint

localhost_url = 'http://localhost:8000/'
base_url = 'https://api.instagram.com/'

def get_access_token():
    auth_route = 'oauth/authorize/'
    scopes = ['basic', 'public_content', 'comments', 'relationships', 'likes', 'follower_list']
    access_token_params = {
        'client_id': CLIENT_ID,
        'redirect_uri': localhost_url,
        'response_type': 'token',
        'scope': ' '.join(scopes)
    }

    res = requests.get(base_url + auth_route, access_token_params)
    for resp in res.history:
        print(resp.status_code, resp.url)
    print(res.status_code, res.url)