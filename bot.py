import os
import json
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  # example: -1002896194875

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Load file mapping from data.json
with open("data.json", "r") as f:
    file_data = json.load(f)

@app.on_message(filters.command("start"))
async def start(client, message):
    args = message.text.split(" ")
    if len(args) > 1:
        file_code = args[1]
        file_id = file_data.get(file_code)
        if file_id:
            try:
                await client.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=CHANNEL_ID,
                    message_id=file_id
                )
            except Exception as e:
                await message.reply(f"❌ ফাইল ফরওয়ার্ড করতে সমস্যা হয়েছে:\n`{e}`")
        else:
            await message.reply("❌ ফাইল পাওয়া যায়নি। ভুল লিংক হতে পারে।")
    else:
        await message.reply("👋 হ্যালো! লিংকের মাধ্যমে ফাইল পেতে আমাকে সঠিক লিংক দিয়ে start করুন।")

app.run()
