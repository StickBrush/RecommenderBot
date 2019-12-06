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

class Genre(Enum):
    """Anime genres as defined by Jikan"""
    ACTION = 1
    ADVENTURE = 2
    CARS = 3
    COMEDY = 4
    DEMENTIA = 5
    DEMONS = 6
    MYSTERY = 7
    DRAMA = 8
    ECCHI = 9
    FANTASY = 10
    GAME = 11
    HENTAI = 12
    HISTORICAL = 13
    HORROR = 14
    MAGIC = 16
    MARTIAL_ARTS = 17
    MECHA = 18
    MUSIC = 19
    PARODY = 20
    SAMURAI = 21
    ROMANCE = 22
    SCHOOL = 23
    SCI_FI = 24
    SHOJO = 25
    SHOJO_AI = 26
    SHONEN = 27
    SHONEN_AI = 28
    SPACE = 29
    SPORTS = 30
    SUPER_POWER = 31
    VAMPIRE = 32
    YAOI = 33
    YURI = 34
    HAREM = 35
    SLICE_OF_LIFE = 36
    SUPERNATURAL = 37
    MILITARY = 38
    POLICE = 39
    PSYCHOLOGICAL = 40
    THRILLER = 41
    SEINEN = 42
    JOSEI = 43

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
        request_url = "{}/1/{}".format(request_url, subtype.value)
    api_response = requests.get(request_url)
    if api_response is not None:
        logging.debug('API response: {}'.format(api_response.json()))
        json_response = api_response.json()
        shows = json_response['top']
        show_ndx = randrange(0, len(shows))
        show = shows[show_ndx]
        return Anime.from_dict(show)

def get_anime_by_genre(genre: Genre) -> Anime:
    """Get a random anime by genre.

    Keyword arguments:
    genre -- Genre of anime to check.
    """
    endpoint = "genre/anime"
    request_url = "{}/{}/{}/1".format(API_BASE_PATH, endpoint, genre.value)
    api_response = requests.get(request_url)
    if api_response is not None:
        logging.debug('API response: {}'.format(api_response.json()))
        json_response = api_response.json()
        shows = json_response['anime']
        show_ndx = randrange(0, len(shows))
        show = shows[show_ndx]
        return Anime.from_dict(show)
        
