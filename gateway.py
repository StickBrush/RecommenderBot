import requests
from enum import Enum
from random import randrange
import logging

from model import Anime

API_BASE_PATH = "https://api.jikan.moe/v3"

class Subtype(Enum):
    """Anime subtype as defined by Jikan"""
    AIRING = "airing"
    UPCOMING = "upcoming"
    TV = "tv"
    MOVIE = "movie"
    OVA = "ova"
    SPECIAL = "special"

def get_subtypes():
    """Get all available subtypes"""
    subtypes = []
    for subtype in Subtype:
        subtypes.append(subtype.value)
    return subtypes

def get_best_anime(subtype: Subtype=None) -> Anime:
    """Get a random best anime.
    
    Keyword arguments:
    subtype -- Subtype of anime to check (default None)
    """
    endpoint = "top/anime"
    request_url = "{}/{}".format(API_BASE_PATH, endpoint)
    if subtype is not None:
        request_url = "{}/{}".format(request_url, subtype.value)
    api_response = requests.get(request_url)
    if api_response is not None:
        logging.debug('API response: {}'.format(api_response.json()))
        json_response = api_response.json()
        shows = json_response['top']
        show_ndx = randrange(0, len(shows))
        show = shows[show_ndx]
        return Anime.from_dict(show)
        