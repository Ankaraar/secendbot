from aiogram import Bot, Dispatcher, types, executor
from keyboard.keyboards import get_keyboard_1, get_keyboard_2
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
api_key = '6767940798:AAGA8rRP9qoY_gRmlqLAfX0UvInHM8adKJI'

bot = Bot(token= api_key)
dp = Dispatcher(bot)

keyboard_inline = InlineKeyboardMarkup(row_width= 1)
but_inline = InlineKeyboardButton('Посмотреть', url='https://www.purina.ru/cats/getting-a-new-cat/finding-the-right-cat-for-me/the-most-beautiful-cats')
but_inline2 = InlineKeyboardButton('Посмотреть', url='https://www.purina.ru/cats/getting-a-new-cat/finding-the-right-cat-for-me/the-most-beautiful-cats')
keyboard_inline.add(but_inline, but_inline2)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, с чем может помочь наш бота'),
        types.BotCommand(command='/hi', description='Здарова!'),
        types.BotCommand(command='/stop', description='Команда для того, чтобы закрыть бота')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет, я твой первый бот!', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://wp-s.ru/wallpapers/0/17/529196211350601/ryzhij-kotik-krupnym-planom.jpg', caption='Вот тебе кот!', reply_markup=keyboard_inline)

@dp.message_handler(lambda message: message.text == 'Перейти на след. клаву')
async def button_2_click(message: types.Message):
    await message.answer('Далее...', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://wp-s.ru/wallpapers/6/5/546384455911008/sobaka-smotryashhaya-v-kadr-na-fone-neba.jpg', caption='Вот тебе собака!')

@dp.message_handler(lambda message: message.text == 'Вернуться на пред. клаву')
async def button_2_click(message: types.Message):
    await message.answer('Далее...', reply_markup= get_keyboard_1())


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с ......')

@dp.message_handler(commands='hi')
async def hi(message: types.Message):
    await message.reply('Приветствую!')

@dp.message_handler(commands='stop')
async def stop(message: types.Message):
    await message.reply('Ладно, молчу.')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
