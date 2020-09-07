from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import config
import getClasses
import getLinks

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


one_inst = getClasses.Rozklad()

two_inst = getLinks.Google(getLinks.username, getLinks.password)
two_inst.login()
toa = two_inst.get_link('https://classroom.google.com/u/1/c/MTUxNjg0Nzk1NDgw')
moac = two_inst.get_link('https://classroom.google.com/u/1/c/MTUyOTA5NzE0MzM2')
two_inst.q()
print(toa)
print(moac)

links = [toa, '', moac]

mes = ''

c = 0
for i in one_inst.get_tomorrow().items():
    mes += str(i[0]) + '.\t' + str(i[1]) + '\n' + str(links[c]) + '\n\n'
    c += 1


def chotamzavtra(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_message(chat_id = chat_id, text = mes)

def main():
    updater = Updater(config.token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('chotamzavtra',chotamzavtra))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
