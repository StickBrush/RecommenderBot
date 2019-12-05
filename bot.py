from telegram.ext import Updater, CommandHandler
import re
import os
import logging

from model import Anime
from gateway import get_best_anime, Subtype

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

def main():
    updater = Updater(os.environ.get("API_KEY"))
    debug_log = os.environ.get('DEBUG_LOG', None)
    if debug_log is not None:
        logging.basicConfig(logging.DEBUG)
    else:
        logging.basicConfig(logging.INFO)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('recommend', recommend_anime))
    dispatcher.add_handler(CommandHandler('airing', recommend_airing_anime))
    dispatcher.add_handler(CommandHandler('movie', recommend_movie))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
