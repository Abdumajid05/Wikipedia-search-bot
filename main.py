from telegram.ext import Updater,Dispatcher,CommandHandler,MessageHandler,Filters,CallbackContext
from telegram.update import Update
from telegram.bot import Bot
import settings
import requests
# import os 
# Token=os.environ['TOKEN']

Token=settings.TOKEN

def start(update:Update,context:CallbackContext):
    update.message.reply_text("Salom men wikipedidadan qidiruvchi botman.Meni ishlatish uchun /search komandasini yuboring.")
    context.bot.send_message(chat_id=update.message.chat_id,text="Salom yana bir bor qidirmqochi bo'lgan matningizni /search Amir Temur ko'rinishida qidirishingiz mumkin.")
def search(update:Update,context:CallbackContext):
    args = context.args
    if len(args) == 0:
        update.message.reply_text("Please enter a search query.")
    else:
        search_text = " ".join(args)
        response = requests.get('https://uz.wikipedia.org/w/api.php', {
            'action': 'opensearch',
            'search': search_text,
            'limit': 1,
            'namespace': 0,
            'format': 'json',
        })
        result = response.json()
        link = result[3]
        if len(link):
            update.message.reply_text(f"Siz matn bo'yicha qidiruv natijasi \nWikipedia sahifasi: {link[0]}")
        else:
            update.message.reply_text(f"Wikipedia sahifasi topilmadi: {search_text}")   

updater = Updater(token=Token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(CommandHandler('search',search))
dispatcher.add_handler(MessageHandler(Filters.all,start))
updater.start_polling()
updater.idle()