import logging
import requests
from t import TOKEN
from get_data import *
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = TOKEN

rates = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
dogs = "https://dog.ceo/api/breeds/image/random"

logging.basicConfig(level = logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot = bot)

request1 = requests.get(rates)
request2 = requests.get(dogs)

@dp.message_handler(commands="start")
async def start_messaging(message: types.Message):
    answer = "Hello 👋!\nWelcome to the bot🤖 which gives information about 💹 and photoes of dogs.\n/rates\n/image\n/numbers"
    await message.answer(answer)

@dp.message_handler(commands="rates")
async def give_rates(message: types.Message):
    answer = None
    if request1.status_code == 200:
        answer = get_rates(request = request1, number = 5)
    else:
        answer = 'Error'
    await message.answer(answer)

@dp.message_handler(commands="image")
async def give_dogs_image(message: types.Message):
    answer = None
    if request2.status_code == 200:
        answer = get_images(request = request2)
    else:
        answer = 'Error'
    await message.answer_photo(answer)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
