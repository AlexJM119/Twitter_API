import unittest
import requests
from twitter_api import get_text, get_response, to_json, make_request

CLIENT_ID = 'aRaHc4eMk3inYP4phEv2Razi9'
CLIENT_SECRET = 'Vw0V8fBoTDSWmkKPpzCjgN0RymA4a50kwR3Jnj9nxRPE01gO2T'

URL = 'https://api.twitter.com/oauth2/token'

BASE_URL = 'https://api.twitter.com/2/tweets/'

tweet_id = '1418562793586966528'

database_name = 'TweBase'


class Twitest(unittest.TestCase):

    def test_get_text(self):
        response = get_response(URL, CLIENT_ID, CLIENT_SECRET)
        resp = to_json(response)
        req = make_request(BASE_URL, tweet_id, resp)
        r = to_json(req)
        self.assertNotEqual(get_text(r), "")


if __name__ == '__main__':
    unittest.main()
