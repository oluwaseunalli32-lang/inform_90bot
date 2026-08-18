import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging (helps debugging on Render)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ---------- CONFIG ----------
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found! Set it in Render environment variables.")

# ---- Your welcome image (raw GitHub URL) ----
WELCOME_IMAGE_URL = "https://raw.githubusercontent.com/oluwaseunalli32-lang/inform_90bot/4a0bd34476012571720b38b29fb78d496b7ce123/welcome.png"

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
    logger.info("Bot started polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
