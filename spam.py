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
message = """🎁 Get FREE $UNI Tokens – No KYC, No BS!
💸 Just sign up and start earning instantly.
⏳ Limited spots. Don’t miss out.
👉 Claim Your Airdrop Now https://unich.com/en/airdrop/sign-up?ref=I9K54H """

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
