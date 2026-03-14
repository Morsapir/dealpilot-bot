import os
import asyncio
from telegram import Bot
from supabase import create_client, Client

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

bot = Bot(token=TELEGRAM_BOT_TOKEN)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def save_test_product():
    data = {
        "source": "test",
        "source_product_id": "demo-1",
        "title": "Test Product",
        "category": "test",
        "price": 19.99,
        "old_price": 29.99,
        "rating": 4.6,
        "reviews_count": 120,
        "image_url": "https://example.com/image.jpg",
        "product_url": "https://example.com/product",
        "affiliate_url": "https://example.com/product?aff=dealpilot",
        "score": 88,
        "posted": False
    }
    supabase.table("products").insert(data).execute()


async def send_test_post():
    message = """🔥 DealPilot test post

זה פוסט בדיקה ראשון של הבוט.

אם אתה רואה את זה בערוץ, החיבור ל Telegram עובד."""
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)


async def main():
    save_test_product()
    await send_test_post()
    print("Done")


if __name__ == "__main__":
    asyncio.run(main())
