
import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, db, bot
import filters
import logging

filters.setup(dp)

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = 'Օգտվող'
admin_message = 'Ադմին'


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row(user_message, admin_message)

    await message.answer('''Ողջույն! 👋

🤖 Ես բոտ-խանութ եմ, որը վաճառում է ցանկացած կատեգորիայի ապրանք:
    
🛍️ Կատալոգ գնալու և ձեզ դուր եկած ապրանքներն ընտրելու համար օգտագործեք հրամանը /menu.

💰 Դուք կարող եք համալրել ձեր հաշիվը IDram, Ameriabank, AraratBAnk .

❓ Առաջացել են հարցեր? Խնդիր չկա ։ Հրաման /sos կօգնի կապնվել ադմինի հետ, ով կփորձի հնարավորինս արագ արձագանքել.

🤝 Պատվիրե՞լ նմանատիպ բոտ: Կապվեք մշակողի հետ <a href="https://t.me/Poghosyan1309">Narek Poghosyan</a>, 😊 )))
    ''', reply_markup=markup)


@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):

    cid = message.chat.id
    if cid in config.ADMINS:
        config.ADMINS.remove(cid)

    await message.answer('Օգտվողի ռեժիմը միացված է.', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):

    cid = message.chat.id
    if cid not in config.ADMINS:
        config.ADMINS.append(cid)

    await message.answer('Ադմինի ռեժիմը միացված է.', reply_markup=ReplyKeyboardRemove())


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()

    await bot.delete_webhook()


async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == '__main__':

    if "HEROKU" in list(os.environ.keys()):

        executor.start_webhook(
            dispatcher=dp,
            webhook_path=config.WEBHOOK_PATH,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )

    else:

        executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
