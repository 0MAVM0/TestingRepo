from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕➖ MATH ✖️➗", callback_data="math")
        ]
    ]
)

backward = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Go Back", callback_data="go_back")]
    ]
)
