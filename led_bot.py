from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Feed,Data
import requests #gets data from cloud

name = "sujithsimha"
key = "aio_WkJi64E9A8jSduT8td91LmZaz3h6"
colour={0:'🔴',
        1:'🟢'}

aio = Client(name,key)
# Create a data item with value 10 in the 'Test' feed.


def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,'Led on')
    bot.send_message(chat_id,colour.get(1))
    data = Data(value=1)
    aio.create_data('major', data)

def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,'Led off')
    bot.send_message(chat_id,colour.get(0))
    data = Data(value=0)
    aio.create_data('major', data)


u=Updater('1240384396:AAGSivHipkLAiVUCy-BCaOAOcliniVcpEgA')
dp=u.dispatcher
d=dp.add_handler(CommandHandler('on',on))
k=dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()



