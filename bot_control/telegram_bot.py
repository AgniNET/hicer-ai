from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from brain.groq_controller import query_groq

# ⚠️ Security Tip: In future, use environment variables or config.json for sensitive data

BOT_TOKEN = '7524761611:AAFP48pBLuA1EdFomM0ei5UdcJaXkd5gu8o'
ADMIN_ID = 7665788919  # Your personal Telegram user ID

# Command handler for /ask
def handle_prompt(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        update.message.reply_text("🚫 Unauthorized access.")
        return

    prompt = ' '.join(context.args)
    if not prompt:
        update.message.reply_text("🧠 Usage: /ask your prompt here")
        return

    reply = query_groq(prompt)
    update.message.reply_text(reply)

# Start bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("ask", handle_prompt))
    updater.start_polling()
    print("✅ Hicer AI Telegram Bot is running!")

if __name__ == "__main__":
    main()
