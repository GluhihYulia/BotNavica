from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

# Включаем логирование чтобы видеть ошибки
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        welcome_text = "Привет 👋\nКто ты?"

        keyboard = [
            [InlineKeyboardButton("Взрослый", callback_data="adult")],
            [InlineKeyboardButton("Подросток", callback_data="teen")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Используем эффективный способ отправки сообщения
        if update.message:
            await update.message.reply_text(welcome_text, reply_markup=reply_markup)
        else:
            await update.callback_query.message.reply_text(welcome_text, reply_markup=reply_markup)

    except Exception as e:
        print(f"Ошибка в start: {e}")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        await query.answer()

        if query.data == "adult":
            await query.edit_message_text("Ты выбрал: Взрослый ✅")
        elif query.data == "teen":
            await query.edit_message_text("Ты выбрал: Подросток ✅")

    except Exception as e:
        print(f"Ошибка в button_handler: {e}")

def main():
    try:
        # Замените токен на свой
        TOKEN = "8440906881:AAEHXC3JNzdIccA7-DyGXxzCw0VQFU4DM1k"

        app = Application.builder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button_handler))

        print("Бот запущен...")
        app.run_polling()

    except Exception as e:
        print(f"Ошибка запуска: {e}")

if __name__ == "__main__":
    main()
