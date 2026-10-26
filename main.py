import os
import telebot
from flask import Flask
from threading import Thread
from telebot import types

BOT_TOKEN = "8904838891:AAFGA45n5BziW08dKvRureqhXZRbrgMjIQo"
ADMIN_ID = 7822879250

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Lxz iOS Bot Running 24/7"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

users_db = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in users_db:
        users_db[user_id] = {"sal
