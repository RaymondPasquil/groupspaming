import time
import os
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Your Telegram credentials
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

# Message you want to send
message = """🚨 LIMITED ACCESS ALERT 🚨
Want exclusive content from Ximena Mendez? 💋
Her private world is now open — but only for a short time.

🔥 Early access, spicy surprises, and no filters.
💎 Get in before the doors close:
👉 https://whop.com/ximena-mendez?a=topwingman

⏳ Don’t wait. This is your invite — she’s waiting."""

# Telegram group usernames
groups = ['@pogohiringg', '@POGOENCODERJOBHIRING',"@sonchi2203","@hiringOFM","@whalesofmjobs"]

# Start the client
with TelegramClient('user_session', api_id, api_hash) as client:
    while True:
        for group in groups:
            try:
                client.send_message(group, message)
                print(f"✅ Message sent to {group}")
            except FloodWaitError as e:
                print(f"⏱️ Rate limited. Waiting {e.seconds} seconds.")
                time.sleep(e.seconds)
            except Exception as e:
                print(f"❌ Failed to send to {group}: {e}")
        print("⏳ Sleeping 10 minutes...")
        time.sleep(30)  # Wait 10 minutes before sending again
