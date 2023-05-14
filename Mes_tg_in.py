from telebot import TeleBot
import summarize
# import flask


# app = flask.Flask(__name__)
# app.secret_key = 'sdfjkgjks23432kldglsdg'

# створення бота
bot = TeleBot('5846205215:AAEpQ20MlelVE4bANFA3yh9VPii60_iQGH0')

#функція для повернення команди 
@bot.message_handler(commands=['start'])
def main(message):                                         
    bot.send_message(message.chat.id, "Ви запустили бота")

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    data = callback.data.split(":")
    # print(data)
    if data[0] == 'reply':
        summarize.react(data[1], 2)

    elif data[0] == 'open':
        summarize.react(data[1], 1)

    elif data[0] == 'ignor':
        pass

bot.polling(skip_pending= True)


# @app.route('/webhooks', methods=["POST"])
# def new_messages_webhooks():
#     if flask.request.method == 'POST':
#         body = flask.request.get_json()
#         message_data = body['message']['data']
#         message_data_decoded = base64.urlsafe_b64decode(message_data.encode('UTF-8')).decode('UTF-8')
#         message_data_dict = json.loads(message_data_decoded)
#
#         email = message_data_dict['emailAddress']
#         print("Pub/sub push, new message at:", email)
#         messages_handler()
#
#     return {'success': True, 'message': 'Watch request executed successfully.'}, 200
#