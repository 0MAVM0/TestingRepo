import requests
from random import randint

from loader import dp
from aiogram import types
from keyboards.inline.menu import backward

math = f"http://numbersapi.com/{randint(1, 9999)}/math"

math_request = requests.get(math)

@dp.callback_query_handler(text="math")
async def math_handler(call: types.callback_query):
    text = math_request.content
    await call.message.edit_text(text=text, parse_mode="Markdown", reply_markup=backward)
