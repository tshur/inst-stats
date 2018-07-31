import requests
import json

import credentials as cred
from utils import check, pprint

base_url = 'https://api.instagram.com/'
version = 'v1/'

opts = {
    'access_token': cred.ACCESS_TOKEN
}

def get_user(opts):
    endpoint = 'users/self/'
    res = requests.get(base_url + version + endpoint, opts).json()
    check(res)
    pprint(res['data'])

def get_photos():
    pass

def main():
    # cred.get_access_token()
    get_user(opts)

if __name__ == '__main__':
    main()
