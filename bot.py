import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# ----------------------------------------------------------------
# Get the bot token from environment variables (Render → Env Vars)
TOKEN = os.getenv("BOT_TOKEN")

# ----------------------------------------------------------------
# Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reply to /start command."""
    await update.message.reply_text(
        "✅ Bot is online and ready!\n"
        "You will receive trading signals here."
    )

# Example placeholder for signals (you can expand later)
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 Example signal placeholder.")

# ----------------------------------------------------------------
# Main entry
def main():
    # Build the Application
    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    # Start the bot (replaces Updater/start_polling in v20+)
    app.run_polling()

# ----------------------------------------------------------------
if __name__ == "__main__":
    main()
