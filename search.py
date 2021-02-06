import requests as r
from sys import argv, exit
from base64 import b64encode
import json


def load_authorization_key():
    filename = "auth.key"
    auth_key = ""
    with open(filename, "r") as infile:
        auth_key = infile.read()
    return auth_key[ 0 : len(auth_key) - 1 ]



def get_auth_key():
    headers = {}
    client_id = ""
    client_secret = ""
    with open("client_id.txt", "r") as infile:
        client_id = infile.read()
        client_id = client_id[ 0 : len(client_id) - 1]
    with open("client_secret.txt", "r") as infile:
        client_secret = infile.read()
        client_secret = client_secret[ 0 : len(client_secret) - 1]
    client_str = f"{client_id}:{client_secret}"
    client_str_bytes = client_str.encode('ascii')
    client_str = b64encode( client_str_bytes ) 
    client_str = client_str.decode('ascii')
    auth_header = f"Basic {client_str}"
    headers['Authorization'] = auth_header
    data = {
        "grant_type" : "client_credentials"
    }
    url = "https://accounts.spotify.com/api/token"
    myreq = r.post(url, headers=headers, data=data)
    status_code = myreq.status_code 
    content = myreq.content.decode('ascii')
    json_data = json.loads(content)
    access_token = json_data['access_token']
    return access_token



def do_request():
    artist_name = argv[1]
    url = f"https://api.spotify.com/v1/search?type=artist&q={artist_name}"
    headers = {
        "Accept"        : "application/json",
        "Content-Type"  : "application/json",
    }
    auth_key = get_auth_key()
    headers['Authorization'] = f"Bearer {auth_key}"
    myreq = r.get(url, headers=headers)
    content = myreq.content
    status_code = myreq.status_code 
    if status_code != 200:
        print("Error: status code:", status_code)
        exit(-1)
    json_data = json.loads(content)
    #json_str = json.dumps(json_data, indent=2)
    #print(json_str)
    return json_data



def format_json_data(json_data):
    artists = json_data['artists']
    items = artists['items']
    for item in items:
        name = item['name']
        artist_id = item['id']
        genres = ",".join( item['genres'] )
        if genres=="":
            continue
        print(name, artist_id, genres)



def check_params():
    if len(argv)!=2:
        print("Usage: python3 search.py <artist>")
        exit(-1)



def main():
    check_params()
    json_data = do_request()
    format_json_data( json_data ) 



if __name__ == "__main__":
    main()
