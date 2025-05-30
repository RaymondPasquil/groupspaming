import time
import os
from telethon.sync import TelegramClient
from dotenv import load_dotenv

# Load API credentials from .env
load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# Telegram group or channel (use exact @username or invite link if public)
target_group = 'https://t.me/POGOENCODERJOBHIRING'

# Crypto Casino Promo Message
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

#BCGame #CryptoCasino #PlayToEarn #CryptoBonus #LegitRaket #FreeCrypto #OnlineCasino #BTCbonus
"""

# Start sending loop
with TelegramClient('user_session', api_id, api_hash) as client:
    while True:
        try:
            group = client.get_entity(target_group)
            client.send_message(group, message)
            print("✅ Message sent! Waiting 60 seconds...")
            time.sleep(60)
        except Exception as e:
            print(f"❌ Error: {e}")
            break
