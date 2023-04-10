import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Command

API_TOKEN = '6114413617:AAFDdCUHXu0DG3Fgn1GBGL7UJP_VptfOEJo'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Start command
@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Murojaatlar"), types.KeyboardButton("Takliflar"))
    await message.reply("Kerakli bo'limni tanlang:", reply_markup=keyboard)


# Button 1 handler
@dp.message_handler(lambda message: message.text == "Murojaatlar")
async def btn_1(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("OFY raisi", url="https://t.me/+998996804608"),
        types.InlineKeyboardButton("Hokim yordamchisi", url="https://t.me/+998999544455"),
        types.InlineKeyboardButton("Yoshlar yetakchisi", url="https://t.me/+998937712641"),
        types.InlineKeyboardButton("Ayollar faoli", url="https://t.me/+998932868655")
    )
    await message.reply("Siz murojaatlar bo'limini tanladingiz. Kimga murojaat qilmoqchisiz:", reply_markup=keyboard)


# Button 2 handler
@dp.message_handler(lambda message: message.text == "Takliflar")
async def btn_2(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("OFY raisi", url="https://t.me/+998996804608"),
        types.InlineKeyboardButton("Hokim yordamchisi", url="https://t.me/+998999544455"),
        types.InlineKeyboardButton("JK deputati", url="https://t.me/Magic_boy_z")
    )
    await message.reply("Siz takliflar bo'limini tanladingiz. Kimga taklif bildirmoqchisiz:", reply_markup=keyboard)



if __name__ == '__main__':
    # Start the bot
    executor.start_polling(dp, skip_updates=True)
