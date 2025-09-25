import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# === Replace this with YOUR Telegram bot token ===
TOKEN = "8435300268:AAF6qlmsdXEoObUA5X-2cWeWrwo5jPHMQKQ"

# Enable logging (helps you debug if anything goes wrong)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot is now active!\n\n"
        "You will start receiving signals, reports, and notifications here."
    )

# Example signal command
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Example: you can later connect this to MT5/strategy
    await update.message.reply_text(
        "📊 Trade Signal:\n\n"
        "Pair: EURUSD\nDirection: BUY\nEntry: 1.0650\nTP: 1.0750\nSL: 1.0600"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    # Run the bot
    app.run_polling()

if __name__ == "__main__":
    main()
