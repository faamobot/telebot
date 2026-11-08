# Telebot

A small Python Telegram message-forwarding bot experiment. It forwards text messages between the configured owner and friend chats.

## Requirements

- Python 3.10 or newer
- A Telegram bot created through BotFather
- Chat IDs for the owner and friend
- `python-telegram-bot` 20.x

Install the dependency:

```powershell
python -m pip install "python-telegram-bot>=20,<21"
```

## Configure

Set these environment variables in PowerShell (replace the placeholders locally; never commit real values):

```powershell
$env:TELEGRAM_BOT_TOKEN = "your-new-bot-token"
$env:OWNER_CHAT_ID = "your-chat-id"
$env:FRIEND_CHAT_ID = "friend-chat-id"
python .\telebot.py
```

The bot token must be kept private. A token was present in an earlier public revision of this repository; revoke it with BotFather and issue a fresh token before running this code. Removing it from the latest file does not erase it from Git history.

## Behavior and limitations

The bot handles text messages only. Both users must have started a conversation with the bot before it can message them. This is a personal experiment, not a hardened messaging service.
