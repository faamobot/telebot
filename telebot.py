import telegram

# Replace with your bot's API token
BOT_TOKEN = '6837065222:AAH_CDDdaG1KX3hSMCOQUfRY44MiTx-_hqg'

# Replace with your friend's Telegram user ID
FRIEND_USER_ID = '1422500920'

# Replace with your own Telegram chat ID
2122187367 = '2122187367'

bot = telegram.Bot(token=BOT_TOKEN)

def handle_message(update, context):
    message = update.message

    if message.chat_id == FRIEND_USER_ID:  # Check for messages from your friend
        # Forward friend's message to you (individually)
        bot.forward_message(chat_id=2122187367, from_chat_id=FRIEND_USER_ID, message_id=message.message_id)
    else:  # Handle messages from you (the bot owner)
        # Forward your message to your friend
        bot.send_message(chat_id=FRIEND_USER_ID, text=message.text)  # Use send_message for direct chat

updater = telegram.Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, handle_message))

updater.start_polling()
updater.idle()
