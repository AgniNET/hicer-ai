import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from brain.groq_controller import query_groq

# 🔐 Tokens from environment (Render pe use hoga)
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

def handle_prompt(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        update.message.reply_text("🚫 Unauthorized user.")
        return

    prompt = ' '.join(context.args)
    if not prompt:
        update.message.reply_text("❓ Usage: /ask your prompt here")
        return

    reply = query_groq(prompt)
    update.message.reply_text(reply)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("ask", handle_prompt))
    updater.start_polling()
    print("✅ Hicer AI Telegram Bot is running!")

if __name__ == "__main__":
    main()
