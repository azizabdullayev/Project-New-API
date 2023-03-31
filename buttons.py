from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Biz haqimizda"),
            KeyboardButton(text="Kurslar"),
        ]
    ],
    resize_keyboard=True
)
courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Foundation'),
            KeyboardButton(text='BackEnd'),
            KeyboardButton(text='DataScience'),
            KeyboardButton(text='FrontEnd'),
            KeyboardButton(text='Android'),
            KeyboardButton(text='Desing'),
        ],
        [
            KeyboardButton(text='Ortga')
        ],
    ],
    resize_keyboard=True
)
course_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursga obuna bo'lish", callback_data="bolish"),
        ],
    ],
)
malumotlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ma'lumotlarni yuborish", request_contact=True),
        ],
        [
            KeyboardButton(text="Kurslar ro'yhatiga qaytish")
        ],
    ],
    resize_keyboard=True
)
end = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh sahifaga qaytish"),
        ]
    ],
    resize_keyboard=True
)
