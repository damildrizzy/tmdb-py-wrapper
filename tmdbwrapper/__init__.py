import os
import  requests


TMDB_API_KEY = os.environ.get('TMDB_API_KEY') or '20cc5695b1fa537fc74a4377baf6a5c9'

class APIKeyMissingError(Exception):
    pass

if TMDB_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://developers.themoviedb.org/3/getting-started/introduction "
        "for how to retrieve an authentication token from "
        "The Movie Database"
    )

session = requests.session()
session.params = {}
session.params['api_key'] = TMDB_API_KEY

from .tv import Tv


