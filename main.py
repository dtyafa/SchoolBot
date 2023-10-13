from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from DATA import *

bot = Bot(token="6358793399:AAGL6X9lDhBl-lNYV0YDCzZll3ju-7M2jQQ")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add(types.KeyboardButton('/Розклад'))
    markup.add(types.KeyboardButton('/Переглянути ДЗ'))
    markup.add(types.KeyboardButton('/Додати ДЗ'))
    await message.answer('Вітаю ви стали частинкою самого гучного класу в школі №6! Чим можу допомогти?',
                         reply_markup=markup)

@dp.message_handler(commands=['Розклад'])
async def process_arcade_command(message: types.Message):
    await message.answer("Понеділок:\n" + rozclad["Понеділок"])
    await message.answer("Вівторок:\n" + rozclad["Вівторок"])
    await message.answer("Середа:\n" + rozclad["Середа"])
    await message.answer("Четвер:\n" + rozclad["Четвер"])
    await message.answer("П'ятниця:\n" + rozclad["П'ятниця"])

if __name__ == '__main__':
    executor.start_polling(dp)
