import requests
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

CLIENT_ID = 'aRaHc4eMk3inYP4phEv2Razi9'
CLIENT_SECRET = 'Vw0V8fBoTDSWmkKPpzCjgN0RymA4a50kwR3Jnj9nxRPE01gO2T'

URL = 'https://api.twitter.com/oauth2/token'

BASE_URL = 'https://api.twitter.com/2/tweets/'

tweet_id = '1418562793586966528'

database_name = 'TweBase'


def get_response(url, c_id, c_secret):
    return requests.post(url, {
        'grant_type': 'client_credentials',
        'client_id': c_id,
        'client_secret': c_secret
    })

def get_status_code(response):
    return response.status_code

def to_json(response):
    return response.json()

def make_request(base, tweet, json_input):
    head = {'Authorization': 'Bearer {token}'.format(token=json_input['access_token'])}
    return requests.get(base + tweet, headers=head)

def create_dataframe(request_input):
    df = pd.DataFrame.from_dict(request_input)
    return df

def start_engine(db, db_name):
    engine = create_engine(f'mysql://root:codio@localhost/{db_name}')
    db.to_sql('tweet_data', con=engine, if_exists='replace', index=False)

def get_text(req_json):
    return req_json['data']['text']

response = get_response(url=URL, c_id=CLIENT_ID, c_secret=CLIENT_SECRET)
print(get_status_code(response))

resp = to_json(response)

req = make_request(BASE_URL, tweet_id, resp)
r = to_json(req)

twedata = create_dataframe(r)
start_engine(twedata, database_name)
