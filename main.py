import os
import re
import json
import requests
import time
import random
import string
import telebot
from telebot import types
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
from flask import Flask, request
from threading import Thread

app = Flask('')

stopuser = {}
token = '7314527313:AAHppoLXOz3AD8-EyDrzwH6F7z-md8g0MLA'
bot = telebot.TeleBot(token, parse_mode="HTML")
admin = "6989709226"
command_usage = {}

def reset_command_usage():
		for user_id in command_usage:
				command_usage[user_id] = {'count': 0, 'last_time': None}

@bot.message_handler(commands=["start"])
def start(message):
		def my_function():
				gate = ''
				name = message.from_user.first_name
				with open('data.json', 'r') as file:
						json_data = json.load(file)
				id = message.from_user.id

				try:
						BL = json_data[str(id)]['plan']
				except KeyError:
						BL = '𝗙𝗥𝗘𝗘'
						with open('data.json', 'r') as json_file:
								existing_data = json.load(json_file)
						new_data = {
								str(id): {
										"plan": "𝗙𝗥𝗘𝗘",
										"timer": "none",
								}
						}
						existing_data.update(new_data)
						with open('data.json', 'w') as json_file:
								json.dump(existing_data, json_file, ensure_ascii=False, indent=4)

				if BL == '𝗙𝗥𝗘𝗘':
						keyboard = types.InlineKeyboardMarkup()
						contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥 ✨", url="https://t.me/TIKA_GROUB")
						keyboard.add(contact_button)
						photo_url = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_owQ6FA-oYbYwna4CY3L_C9ppZZY6WZXE-K2ZLEkdioX9j4Py1tHqgBRURscKrN1JaZhKDd2fBTO9r-I43c0d88hnZ43YKrYyTULGcPootsnQ6fsttjsAMoQg15LsP6JEEn_uppEajidRhLaacVV_fMrcrogNyJ8rDhO0U7vMF05mS5LGC_2yz8m4r1U/s734/photo_2024-02-09_17-05-09.jpg'
						bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:

𝑬𝑮𝒀𝑷𝑻 
1 𝑾𝑬𝑬𝑲 > 250𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 600𝑬𝑮

𝑰𝑹𝑨𝑸 
1 𝑾𝑬𝑬𝑲 ➜  6 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  13 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 𝑾𝑬𝑬𝑲 ➜  6$ 
1 𝑴𝑶𝑵𝑻𝑯 ➜  13$

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
						''', reply_markup=keyboard)
						return

				keyboard = types.InlineKeyboardMarkup()
				contact_button = types.InlineKeyboardButton(text="✨ 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/TIKA_GROUB")
				keyboard.add(contact_button)
				photo_url = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_owQ6FA-oYbYwna4CY3L_C9ppZZY6WZXE-K2ZLEkdioX9j4Py1tHqgBRURscKrN1JaZhKDd2fBTO9r-I43c0d88hnZ43YKrYyTULGcPootsnQ6fsttjsAMoQg15LsP6JEEn_uppEajidRhLaacVV_fMrcrogNyJ8rDhO0U7vMF05mS5LGC_2yz8m4r1U/s734/photo_2024-02-09_17-05-09.jpg'
				bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''', reply_markup=keyboard)

		my_thread = threading.Thread(target=my_function)
		my_thread.start()

@bot.message_handler(commands=["cmds"])
def cmds(message):
		with open('data.json', 'r') as file:
				json_data = json.load(file)
		id = message.from_user.id
		try:
				BL = json_data[str(id)]['plan']
		except KeyError:
				BL = '𝗙𝗥𝗘𝗘'
		name = message.from_user.first_name
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"✨ {BL} ✨", callback_data='plan')
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}

𝑯𝑬𝑹𝑬 𝑨𝑹𝑬 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺:

/start ➜ 𝑺𝑻𝑨𝑹𝑻 𝑻𝑯𝑬 𝑩𝑶𝑻
/cmds ➜ 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺
/check ➜ 𝑪𝑯𝑬𝑪𝑲 𝑻𝑯𝑬 𝑪𝑨𝑹𝑫
</b>''', reply_markup=keyboard)

@bot.message_handler(commands=["check"])
def check(message):
		bot.send_message(chat_id=message.chat.id, text="<b>Checking the card...</b>")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
		if call.data == "plan":
				bot.send_message(chat_id=call.message.chat.id, text="<b>Thank you for choosing our service!</b>")

@app.route('/')
def home():
		return "<b>telegram  @l4vl4</b>"

def run():
		app.run(host='0.0.0.0', port=8080)

def keep_alive():
		t = Thread(target=run)
		t.start()

if __name__ == "__main__":
		keep_alive()
		bot.infinity_polling(skip_pending=True)
