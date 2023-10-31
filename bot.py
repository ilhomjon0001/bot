import telebot
from PIL import Image
import requests
from io import BytesIO

TOKEN = ''    # token api bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Assalomu aleykum, {message.from_user.first_name}! Manga rasm jo'nating man sizga 3x4 rasm qilib beraman"
    bot.send_message(message.chat.id, mess)

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    for photo in message.photo:
        file_id = photo.file_id
        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"
        response = requests.get(file_url)
        image = Image.open(BytesIO(response.content))
        image = image.resize((300, 400))
        bot.send_photo(message.chat.id, image)
        break


bot.polling(none_stop=True)
