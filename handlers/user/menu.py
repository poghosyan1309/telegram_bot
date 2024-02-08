
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🛍️ Կատալոգ'
balance = '💰 Հաշիվ'
cart = '🛒 Զամբյուղ'
delivery_status = '🚚 Պատվերի կարգավիճակը'

settings = '⚙️ Կատալոգի կարգավորում'
orders = '🚚 Պատվեր'
questions = '❓ Հարցեր'

@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Մենյու', reply_markup=markup)

@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Մենյու', reply_markup=markup)
