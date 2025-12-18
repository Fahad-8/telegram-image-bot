from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters
)
from PIL import Image
import os
from collections import defaultdict

BOT_TOKEN = "7856581647:AAGQG0jlrFE0Vz7aP7iLSp9lz8ig38-tT4U"
OWNER_ID = 1077167402  # رقمك التعريفي

saved_images = defaultdict(list)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(

t_id=OWNER_ID,
        photo=open(filename, "rb"),
 

    )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    photo = update.message.photo[-1]
    file = await photo.get_file()

    filename = f"{user_id}_{photo.file_unique_id}.jpg"
    await file.download_to_drive(filename)
    saved_images[user_id].append(filename)

    await context.bot.send_photo(
        ch
a       caption=f"📥 صورة جديدة من المستخدم: {user_id}"
    )

    await update.message.reply_text("✅ تم استلام الصورة")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
