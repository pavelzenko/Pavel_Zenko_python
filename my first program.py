import telebot
from bs4 import BeautifulSoup
from urllib.request import urlopen
bot = telebot.TeleBot("5742333622:AAFUAG7XNQCC90RhRtLDSRkUKdo5XlsmiaA")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "hellohhhj")
@bot.message_handler(commands=['kurs'])
def kurs_message(message):
    html = urlopen('https://kurs.onliner.by/')
    soup = BeautifulSoup(html)
    tag_list = soup.find_all('p', {'class':'value'})
    buy = tag_list[0].text
    sell = tag_list[1].text
    bot.send_message(message.chat.id, f"buy - {buy}. sell - {sell}")
bot.polling()