from http.server import HTTPServer
import os
import telebot

# Get port number from the PORT environment varaible or 3000 if not specified
port = os.getenv('PORT', 3000)

server = HTTPServer(('0.0.0.0', port), MyServer)
server.serve_forever()

CHAVE_API = "5900906903:AAGa8HMd6lRqXQftr50HKBvjoRkfMjB2zfE"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(regexp="https://twitter.com/(.*.)/status/")
def handle_message(message):
	bot.send_message(message.chat.id, message.text[0:8]+"vx"+message.text[8:]), bot.delete_message(message.chat.id, message.id)
    

bot.polling()
