import telebot

CHAVE_API = "5900906903:AAGa8HMd6lRqXQftr50HKBvjoRkfMjB2zfE"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(regexp="https://twitter.com/(.*.)/status/")
def handle_message(message):
	bot.send_message(message.chat.id, message.text[0:8]+"vx"+message.text[8:]), bot.delete_message(message.chat.id, message.id)
    

bot.polling()