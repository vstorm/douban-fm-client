import os
import json

from client import DoubanFmClient


username = "your username"
password = "your password"
API_KEY = "your api key"
API_SECRET = "your api secret"
REDIRECT_URL = "http://douban.fm"

client = DoubanFmClient(API_KEY, API_SECRET, REDIRECT_URL)
client.auth_with_password(username, password)


def get_file_path(filename):
    dir_path = os.path.join(os.path.abspath(".."), "tmp")
    return os.path.join(dir_path, filename)


def write_to_file(file_path, d):
    with open(file_path, "wt") as f:
        json.dump(d, f, ensure_ascii=False,
                  indent=4, separators=(',', ': '))