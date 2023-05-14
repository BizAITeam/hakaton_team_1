from telebot import TeleBot, types
from GmailOpen_GmailReply import open_gmail_message

bot = TeleBot('5846205215:AAEpQ20MlelVE4bANFA3yh9VPii60_iQGH0')
CHAT_ID = '463210327'

def format_message(chat_id, text, action_list):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for action in action_list:

        if action['type'] == 1:
            url_email = types.InlineKeyboardButton(text = 'Open e-mail', url=open_gmail_message(action['id']))
            keyboard.add(url_email)
        if action['type'] == 0:
            ignor_message = types.InlineKeyboardButton(text = 'Ignor a letter', callback_data='ignor:test')
            keyboard.add(ignor_message)
        if action['type'] == 2:
            reply_message = types.InlineKeyboardButton(
                text='Reply a letter',
                callback_data=f"reply:{action['id']}"
            )
            keyboard.add(reply_message)

    bot.send_message(CHAT_ID, text, reply_markup=keyboard)

