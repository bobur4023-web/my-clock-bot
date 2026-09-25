import asyncio
import os
from datetime import datetime
import pytz
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession

api_id = 39948328
api_hash = '31d3a0bd2a50061bc84665e3013daf4a'
session_string = os.environ.get("SESSION_STRING")

# Toshkent vaqt zonasi
timezone = pytz.timezone('Asia/Tashkent')

async def main():
    async with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        print("Bot muvaffaqiyatli ishga tushdi!")
        prev_time = ""
        while True:
            try:
                current_time = datetime.now(timezone).strftime("%H:%M")
                if current_time != prev_time:
                    new_name = f"Umid {current_time}"
                    await client(UpdateProfileRequest(first_name=new_name))
                    prev_time = current_time
                    print(f"Ism yangilandi: {new_name}")
            except Exception as e:
                print(f"Xatolik: {e}")
            
            await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())
