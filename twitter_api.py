import requests 

CLIENT_ID = 'aRaHc4eMk3inYP4phEv2Razi9'
CLIENT_SECRET = 'Vw0V8fBoTDSWmkKPpzCjgN0RymA4a50kwR3Jnj9nxRPE01gO2T'

URL = 'https://api.twitter.com/oauth2/token'
auth_response = requests.post(URL, {
    'grant_type' : 'client_credentials', 
    'client_id': CLIENT_ID, 
    'client_secret': CLIENT_SECRET
})
print(auth_response.status_code)

auth_response_data = auth_response.json()
print(auth_response_data)

access_token = auth_response_data['access_token']

headers = {
    'Authorization' : 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.twitter.com/2/tweets/'

tweet_id = '1417431102390603776'

r = requests.get(BASE_URL + tweet_id, headers=headers)
r = r.json()
print(f"\nTweet Specs\nid : {r['data']['id']}\ntext: {r['data']['text']}")

