import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging (helps you debug on Render)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ---------- CONFIGURATION ----------
# Get the token from environment variables (safe for Render)
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found! Set it in Render environment variables.")

# WELCOME IMAGE – Upload your image to imgur.com, postimages.org, or your own hosting
# and paste the DIRECT URL (ends with .jpg, .png, etc.) here.
WELCOME_IMAGE_URL = os.getenv("WELCOME_IMAGE_URL", "https://your-image-url.com/welcome.jpg")

WELCOME_CAPTION = (
    "🚀 Welcome to Paisa Base!\n\n"
    "Click the buttons below to get started:"
)

# ---------- BUTTONS ----------
KEYBOARD = [
    [InlineKeyboardButton("📝 Register", url="https://wallet.paisa-base.com/register?inviteCode=phar6p")],
    [InlineKeyboardButton("📢 Channel", url="https://t.me/+oTUFYl-kubM1OTU1")],
    [InlineKeyboardButton("📞 Contact Support", url="https://t.me/jetlee261")],
]
REPLY_MARKUP = InlineKeyboardMarkup(KEYBOARD)

# ---------- /start COMMAND ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    logger.info(f"User {user.id} ({user.username}) started the bot.")

    await update.message.reply_photo(
        photo=WELCOME_IMAGE_URL,
        caption=WELCOME_CAPTION,
        reply_markup=REPLY_MARKUP,
    )

# ---------- MAIN ----------
def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Start polling (works perfectly on Render's background worker)
    logger.info("Bot started polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
