from telegram.ext import Updater, CommandHandler
import re
import os
import logging

from model import Anime
from gateway import *

def recommend_anime(bot, update):
    logging.debug('Received recommendation request')
    anime = get_best_anime().to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_airing_anime(bot, update):
    logging.debug('Received airing request')
    anime = get_best_anime(subtype=Subtype.AIRING).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_movie(bot, update):
    logging.debug('Received movie request')
    anime = get_best_anime(subtype=Subtype.MOVIE).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_action_anime(bot, update):
    logging.debug('Received action request')
    anime = get_anime_by_genre(Genre.ACTION).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_adventure_anime(bot, update):
    logging.debug('Received adventure request')
    anime = get_anime_by_genre(Genre.ADVENTURE).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_cars_anime(bot, update):
    logging.debug('Received cars request')
    anime = get_anime_by_genre(Genre.CARS).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_comedy_anime(bot, update):
    logging.debug('Received comedy request')
    anime = get_anime_by_genre(Genre.COMEDY).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_dementia_anime(bot, update):
    logging.debug('Received dementia request')
    anime = get_anime_by_genre(Genre.DEMENTIA).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_demons_anime(bot, update):
    logging.debug('Received demons request')
    anime = get_anime_by_genre(Genre.DEMONS).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_mystery_anime(bot, update):
    logging.debug('Received mystery request')
    anime = get_anime_by_genre(Genre.MYSTERY).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_drama_anime(bot, update):
    logging.debug('Received drama request')
    anime = get_anime_by_genre(Genre.DRAMA).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_ecchi_anime(bot, update):
    logging.debug('Received ecchi request')
    anime = get_anime_by_genre(Genre.ECCHI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_fantasy_anime(bot, update):
    logging.debug('Received fantasy request')
    anime = get_anime_by_genre(Genre.FANTASY).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_game_anime(bot, update):
    logging.debug('Received game request')
    anime = get_anime_by_genre(Genre.GAME).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_hentai_anime(bot, update):
    logging.debug('Received hentai request')
    anime = get_anime_by_genre(Genre.HENTAI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_historical_anime(bot, update):
    logging.debug('Received historical request')
    anime = get_anime_by_genre(Genre.HISTORICAL).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_horror_anime(bot, update):
    logging.debug('Received horror request')
    anime = get_anime_by_genre(Genre.HORROR).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_magic_anime(bot, update):
    logging.debug('Received magic request')
    anime = get_anime_by_genre(Genre.MAGIC).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_martial_arts_anime(bot, update):
    logging.debug('Received martial arts request')
    anime = get_anime_by_genre(Genre.MARTIAL_ARTS).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_mecha_anime(bot, update):
    logging.debug('Received mecha request')
    anime = get_anime_by_genre(Genre.MECHA).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_music_anime(bot, update):
    logging.debug('Received music request')
    anime = get_anime_by_genre(Genre.MUSIC).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_parody_anime(bot, update):
    logging.debug('Received parody request')
    anime = get_anime_by_genre(Genre.PARODY).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_samurai_anime(bot, update):
    logging.debug('Received samurai request')
    anime = get_anime_by_genre(Genre.SAMURAI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_romance_anime(bot, update):
    logging.debug('Received romance request')
    anime = get_anime_by_genre(Genre.ROMANCE).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_school_anime(bot, update):
    logging.debug('Received school request')
    anime = get_anime_by_genre(Genre.SCHOOL).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_sci_fi_anime(bot, update):
    logging.debug('Received sci-fi request')
    anime = get_anime_by_genre(Genre.SCI_FI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_shojo_anime(bot, update):
    logging.debug('Received shojo request')
    anime = get_anime_by_genre(Genre.SHOJO).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_shojo_ai_anime(bot, update):
    logging.debug('Received shojo-ai request')
    anime = get_anime_by_genre(Genre.SHOJO_AI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_shonen_anime(bot, update):
    logging.debug('Received shonen request')
    anime = get_anime_by_genre(Genre.SHONEN).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_shonen_ai_anime(bot, update):
    logging.debug('Received shonen-ai request')
    anime = get_anime_by_genre(Genre.SHONEN_AI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_space_anime(bot, update):
    logging.debug('Received space request')
    anime = get_anime_by_genre(Genre.SPACE).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_sports_anime(bot, update):
    logging.debug('Received sports request')
    anime = get_anime_by_genre(Genre.SPORTS).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_super_power_anime(bot, update):
    logging.debug('Received super power request')
    anime = get_anime_by_genre(Genre.SUPER_POWER).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_vampire_anime(bot, update):
    logging.debug('Received vampire request')
    anime = get_anime_by_genre(Genre.VAMPIRE).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_yaoi_anime(bot, update):
    logging.debug('Received yaoi request')
    anime = get_anime_by_genre(Genre.YAOI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_yuri_anime(bot, update):
    logging.debug('Received yuri request')
    anime = get_anime_by_genre(Genre.YURI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_harem_anime(bot, update):
    logging.debug('Received harem request')
    anime = get_anime_by_genre(Genre.HAREM).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_slice_of_life_anime(bot, update):
    logging.debug('Received slice of life request')
    anime = get_anime_by_genre(Genre.SLICE_OF_LIFE).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_supernatural_anime(bot, update):
    logging.debug('Received supernatural request')
    anime = get_anime_by_genre(Genre.SUPERNATURAL).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_military_anime(bot, update):
    logging.debug('Received military request')
    anime = get_anime_by_genre(Genre.MILITARY).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_police_anime(bot, update):
    logging.debug('Received police request')
    anime = get_anime_by_genre(Genre.POLICE).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_psychological_anime(bot, update):
    logging.debug('Received psychological request')
    anime = get_anime_by_genre(Genre.PSYCHOLOGICAL).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_thriller_anime(bot, update):
    logging.debug('Received thriller request')
    anime = get_anime_by_genre(Genre.THRILLER).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_seinen_anime(bot, update):
    logging.debug('Received seinen request')
    anime = get_anime_by_genre(Genre.SEINEN).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def recommend_josei_anime(bot, update):
    logging.debug('Received josei request')
    anime = get_anime_by_genre(Genre.JOSEI).to_prettified_dict()
    logging.debug('Answer: '.format(anime))
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def main():
    updater = Updater(os.environ.get("API_KEY"))
    debug_log = os.environ.get('DEBUG_LOG', None)
    if debug_log is not None:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('recommend', recommend_anime))
    dispatcher.add_handler(CommandHandler('airing', recommend_airing_anime))
    dispatcher.add_handler(CommandHandler('movie', recommend_movie))
    dispatcher.add_handler(CommandHandler('action', recommend_action_anime))
    dispatcher.add_handler(CommandHandler('adventure', recommend_adventure_anime))
    dispatcher.add_handler(CommandHandler('cars', recommend_cars_anime))
    dispatcher.add_handler(CommandHandler('comedy', recommend_comedy_anime))
    dispatcher.add_handler(CommandHandler('dementia', recommend_dementia_anime))
    dispatcher.add_handler(CommandHandler('demons', recommend_demons_anime))
    dispatcher.add_handler(CommandHandler('mystery', recommend_mystery_anime))
    dispatcher.add_handler(CommandHandler('drama', recommend_drama_anime))
    dispatcher.add_handler(CommandHandler('ecchi', recommend_ecchi_anime))
    dispatcher.add_handler(CommandHandler('fantasy', recommend_fantasy_anime))
    dispatcher.add_handler(CommandHandler('game', recommend_game_anime))
    dispatcher.add_handler(CommandHandler('hentai', recommend_hentai_anime))
    dispatcher.add_handler(CommandHandler('historical', recommend_historical_anime))
    dispatcher.add_handler(CommandHandler('horror', recommend_horror_anime))
    dispatcher.add_handler(CommandHandler('magic', recommend_magic_anime))
    dispatcher.add_handler(CommandHandler('martialarts', recommend_martial_arts_anime))
    dispatcher.add_handler(CommandHandler('mecha', recommend_mecha_anime))
    dispatcher.add_handler(CommandHandler('music', recommend_music_anime))
    dispatcher.add_handler(CommandHandler('parody', recommend_parody_anime))
    dispatcher.add_handler(CommandHandler('samurai', recommend_samurai_anime))
    dispatcher.add_handler(CommandHandler('romance', recommend_romance_anime))
    dispatcher.add_handler(CommandHandler('school', recommend_school_anime))
    dispatcher.add_handler(CommandHandler('scifi', recommend_sci_fi_anime))
    dispatcher.add_handler(CommandHandler('shojo', recommend_shojo_anime))
    dispatcher.add_handler(CommandHandler('shoujo', recommend_shojo_anime))
    dispatcher.add_handler(CommandHandler('shojoai', recommend_shojo_ai_anime))
    dispatcher.add_handler(CommandHandler('shoujoai', recommend_shojo_ai_anime))
    dispatcher.add_handler(CommandHandler('shonen', recommend_shonen_anime))
    dispatcher.add_handler(CommandHandler('shounen', recommend_shonen_anime))
    dispatcher.add_handler(CommandHandler('shonenai', recommend_shonen_ai_anime))
    dispatcher.add_handler(CommandHandler('shounenai', recommend_shonen_ai_anime))
    dispatcher.add_handler(CommandHandler('space', recommend_space_anime))
    dispatcher.add_handler(CommandHandler('sports', recommend_sports_anime))
    dispatcher.add_handler(CommandHandler('superpower', recommend_super_power_anime))
    dispatcher.add_handler(CommandHandler('vampire', recommend_vampire_anime))
    dispatcher.add_handler(CommandHandler('yaoi', recommend_yaoi_anime))
    dispatcher.add_handler(CommandHandler('yuri', recommend_yuri_anime))
    dispatcher.add_handler(CommandHandler('harem', recommend_harem_anime))
    dispatcher.add_handler(CommandHandler('sliceoflife', recommend_slice_of_life_anime))
    dispatcher.add_handler(CommandHandler('supernatural', recommend_supernatural_anime))
    dispatcher.add_handler(CommandHandler('military', recommend_military_anime))
    dispatcher.add_handler(CommandHandler('police', recommend_police_anime))
    dispatcher.add_handler(CommandHandler('psychological', recommend_psychological_anime))
    dispatcher.add_handler(CommandHandler('thriller', recommend_thriller_anime))
    dispatcher.add_handler(CommandHandler('seinen', recommend_seinen_anime))
    dispatcher.add_handler(CommandHandler('josei', recommend_josei_anime))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
