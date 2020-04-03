from telegram.ext import Updater, CommandHandler
from config.auth import token
from random import randint, uniform,random

import logging

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger('dbm_python_bot')

def start(bot, update):
    logger.info('He recibido un comando start')
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Hey!! ¿Conoces la función generadora de combinaciones de bonoloto?"
    )
    logger.warning('Esto ya no es tan normal')

def bonoloto(bot, update):
    logger.info('He recibido un comando bonoloto, desde: ' + str(update.message.chat_id))    
    mens = ''
    numeros = list()
    for x in range(6):
        azar = randint(1,49)
        while(azar in numeros):
            azar = randint(1,49)
        numeros.append(azar)
        mens = mens + str(azar)
        if x < 5:
            mens = mens + " # "
    
    bot.send_message(
        chat_id = update.message.chat_id,
        text = mens
    )

if __name__ == '__main__':

    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    dispatcher.add_handler(CommandHandler('bonoloto', bonoloto))

    updater.start_polling()
    updater.idle()