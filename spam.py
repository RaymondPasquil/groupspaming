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
message = """🎰 LEGIT CRYPTO CASINO + FREE BONUS! 🎁
Looking for a trusted play-to-earn crypto game?
🔥 BC.Game is 100% legit — with real payouts, fast crypto withdrawals, and tons of games (slots, crash, roulette, etc.)

💸 Get FREE rewards when you register using my link or referral code!
✅ Daily bonus spins
✅ Welcome packages
✅ Up to 1 BTC bonus!

🎯 Sign Up Now:
🔗 https://bcgame0.com/i-3bw1uxxla-n/

OR
🆔 Use Referral Code: 3bw1uxxla at registration!

🚀 Join the hype and start winning crypto today!
💬 DM me if you need help getting started. Happy to guide!

#BCGame #CryptoCasino #PlayToEarn #CryptoBonus #LegitRaket #FreeCrypto #OnlineCasino #BTCbonus"""

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
