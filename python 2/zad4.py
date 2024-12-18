from aiogram import Bot, Dispatcher, types
from aiogram import Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
import asyncio
 
API_TOKEN = '7930573531:AAGoF19KEv6oIPETPp3TN0v-bc3NMLD26AA'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
 
start_router = Router()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    kb_list = [
        [KeyboardButton(text="📖 О нас")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
    await message.answer("Привет!\nЯ бот\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=keyboard)



@dp.message(F.text == "📖 О нас")
async def ease_link_kb(message: types.Message):
    inline_kb_list = [
        [InlineKeyboardButton(text="Купите мне", url='https://store.steampowered.com/app/431960/Wallpaper_Engine/')],
        [InlineKeyboardButton(text="Мой ТГ", url='tg://resolve?domain=morsals1')],
        [InlineKeyboardButton(text="Раздача гта 6", web_app=WebAppInfo(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
    await message.answer('Вот тебе инлайн клавиатура со ссылками!', reply_markup=keyboard)

@dp.message(Command('p'))
async def send_welcome(message: types.Message):
   await message.answer("Я пошел в баню")


async def on_start():
   await dp.start_polling(bot)
   await cmd_start
 
if __name__ == '__main__':
   asyncio.run(on_start())