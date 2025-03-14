import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler
from telegram import ReplyKeyboardMarkup

# Загружаем переменные окружения
load_dotenv()

# Получаем токен бота
TOKEN = os.getenv('BOT_TOKEN')

# Определяем состояния разговора
CHOOSING, TYPING_REPLY = range(2)

async def start(update, context):
    """Начало разговора"""
    keyboard = [
        ['📅 Расписание', '🍎 Калории'],
        ['💰 Финансы', '❓ Помощь']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        'Привет! Я твой личный помощник. Выбери нужный раздел:',
        reply_markup=reply_markup
    )
    return CHOOSING

async def help_command(update, context):
    """Помощь"""
    help_text = """
    Доступные команды:
    /start - Начать работу
    /help - Показать это сообщение
    """
    await update.message.reply_text(help_text)

def main():
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
