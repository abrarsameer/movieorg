import os
import json
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Load file mapping from data.json
with open("data.json", "r") as f:
    file_data = json.load(f)

@app.on_message(filters.command("start"))
async def start(client, message):
    args = message.text.split(" ")
    if len(args) > 1:
        file_code = args[1]
        file_info = file_data.get(file_code)

        if file_info:
            try:
                message_id = file_info["message_id"]
                channel_id = int(file_info["channel_id"])
                
                await client.copy_message(
                    chat_id=message.chat.id,
                    from_chat_id=channel_id,
                    message_id=message_id
                )
            except Exception as e:
                await message.reply(f"❌ ফাইল পাঠাতে সমস্যা:\n`{e}`")
        else:
            await message.reply("❌ ফাইল পাওয়া যায়নি! ভুল লিংক হতে পারে।")
    else:
        await message.reply("👋 হ্যালো! লিংক সহ /start দিন (যেমন `/start movieorg0002`) ফাইল পেতে।")

app.run()
