from telegram.ext import Updater, CommandHandler
import re
import os

from model import Anime
from gateway import get_best_anime

def recommend_anime(bot, update):
    anime = get_best_anime().to_prettified_dict()
    chat_id = update.message.chat_id
    image = anime.pop('Image')
    caption = '{}\n'.format(anime.pop('Title'))
    for key in anime:
        caption += '{}: {}\n'.format(key, anime[key])
    bot.send_photo(chat_id=chat_id, photo=image, caption=caption)

def main():
    updater = Updater(os.environ.get("API_KEY"))
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('recommend', recommend_anime))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()