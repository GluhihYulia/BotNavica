from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging
import asyncio

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = "Привет 👋\nКто ты?"
    
    keyboard = [
        [InlineKeyboardButton("Взрослый", callback_data="adult")],
        [InlineKeyboardButton("Подросток", callback_data="teen")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "adult":
        await query.edit_message_text("Ты выбрал: Взрослый ✅")
    elif query.data == "teen":
        await query.edit_message_text("Ты выбрал: Подросток ✅")

async def main():
    # Создаём приложение
    TOKEN = "8440906881:AAEHXC3JNzdIccA7-DyGXxzCw0VQFU4DM1k"
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Запускаем бота
    print("Бот запущен и работает!")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
