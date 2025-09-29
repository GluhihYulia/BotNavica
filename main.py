from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update: Update, context: CallbackContext):
    welcome_text = "Привет 👋\nКто ты?"
    
    keyboard = [
        [InlineKeyboardButton("Взрослый", callback_data="adult")],
        [InlineKeyboardButton("Подросток", callback_data="teen")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(welcome_text, reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    if query.data == "adult":
        query.edit_message_text("Ты выбрал: Взрослый ✅")
    elif query.data == "teen":
        query.edit_message_text("Ты выбрал: Подросток ✅")

def main():
    # Создаём updater
    TOKEN = "8440906881:AAEHXC3JNzdIccA7-DyGXxzCw0VQFU4DM1k"
    updater = Updater(TOKEN, use_context=True)
    
    # Получаем dispatcher для регистрации обработчиков
    dp = updater.dispatcher
    
    # Регистрируем обработчики
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    
    # Запускаем бота
    print("Бот запущен и работает!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
