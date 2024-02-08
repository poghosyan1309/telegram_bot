from aiogram.types import ReplyKeyboardMarkup

back_message = '👈 Ետ'
confirm_message = '✅ Հաստատեք պատվերը'
all_right_message = '✅ Ամեն ինչ ճիշտ է'
cancel_message = '🚫 Չեղարկել'

def confirm_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(confirm_message)
    markup.add(back_message)

    return markup

def back_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(back_message)

    return markup

def check_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(back_message, all_right_message)

    return markup

def submit_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(cancel_message, all_right_message)

    return markup
