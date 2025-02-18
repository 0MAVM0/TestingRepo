from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.menu import buttons

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f"Hello, *{message.from_user.full_name}*!\n\n"
    text += "```NUMBERS API```\n\n"
    text += "*- What tales do your metrics tell?*\n"
    text += "*- Bring your metrics and dates to life.*\n"
    text += "*- An API BOT for interesting facts about numbers.*\n"
    text += "*- Let your statistics tell tales and dates come to life.*\n"
    await message.answer(text=text, parse_mode="Markdown", reply_markup=buttons)

@dp.callback_query_handler(text="go_back")
async def go_back(call: types.callback_query):
    await call.message.edit_text("You are back in main menu 🎯", reply_markup=buttons)
