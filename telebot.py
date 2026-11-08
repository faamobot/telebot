"""Minimal Telegram message-forwarding bot template.

Set TELEGRAM_BOT_TOKEN, OWNER_CHAT_ID, and FRIEND_CHAT_ID in the environment
before running. Never commit bot tokens or private chat identifiers.
"""
import os

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
OWNER_CHAT_ID = int(os.environ["OWNER_CHAT_ID"])
FRIEND_CHAT_ID = int(os.environ["FRIEND_CHAT_ID"])


async def forward_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message is None or message.text is None:
        return

    if message.chat_id == FRIEND_CHAT_ID:
        await message.forward(chat_id=OWNER_CHAT_ID)
    elif message.chat_id == OWNER_CHAT_ID:
        await context.bot.send_message(chat_id=FRIEND_CHAT_ID, text=message.text)


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_messages))
    app.run_polling()


if __name__ == "__main__":
    main()
