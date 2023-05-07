# from aiogram import Bot, Dispatcher, types, executor
# from dotenv import load_dotenv
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
# import os
# load_dotenv()
#
#
# BOT_TOKEN = os.getenv('token')
# bot = Bot(BOT_TOKEN)
# dp = Dispatcher(bot=bot)
#
# @dp.message_handler(commands=['start','help'])
# async def main_handler(msg:types.Message):
#     await bot.set_my_commands([BotCommand('reply', "reply buttonlarni show qilib beradi"),BotCommand('inline', 'inline buttonlarni show qilib beradi ')])
#     await msg.answer("Assalomu Aleykum")
#     # await msg.reply("Hello")
#     # await msg.bot.send_message(msg.from_user.id, 'Hello2')
#
#
# @dp.message_handler(commands = 'reply')
# async def reply_show_handler(msg:types.Message):
#     design = [
#         ["button1",KeyboardButton('phone',request_contact=True)],
#         ["button2"]
#     ]
#     rkm = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True,keyboard=design)
#     await msg.answer("Show reply button",reply_markup=rkm)
#
# # @dp.message_handler(commands ='inline')
# # async def reply_show_handler(msg: types.Message):
# #     ikm = InlineKeyboardMarkup()
# #     ikm.add(InlineKeyboardButton('1',callback_data='1'))
# #     ikm.add(InlineKeyboardButton('inline1',callback_data='2'))
# #     ikm.add(InlineKeyboardButton('inline1',callback_data='3'))
# #     await msg.answer("Show inline button",reply_markup=ikm)
#
#
# @dp.message_handler(commands ='inline')
# async def reply_show_handler(msg: types.Message):
#     design = [
#         [InlineKeyboardButton('1',callback_data='1'),InlineKeyboardButton('2',callback_data='2'),InlineKeyboardButton('3',callback_data='3'),InlineKeyboardButton('+',callback_data='1')],
#         [InlineKeyboardButton('4',callback_data='4'),InlineKeyboardButton('5',callback_data='5'),InlineKeyboardButton('6',callback_data='6'),InlineKeyboardButton('-',callback_data='1')],
#         [InlineKeyboardButton('7',callback_data='7'),InlineKeyboardButton('8',callback_data='8'),InlineKeyboardButton('9',callback_data='9'),InlineKeyboardButton('/',callback_data='1')],
#         [InlineKeyboardButton('0',callback_data='0'),InlineKeyboardButton('C',callback_data='C'),InlineKeyboardButton('=',callback_data='='),InlineKeyboardButton('*',callback_data='1')],
#     ]
#     ikm = InlineKeyboardMarkup(inline_keyboard=design)
#     await msg.answer("______________",reply_markup=ikm)
#
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
#
#

import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import spoiler, code
from dotenv import load_dotenv
import psycopg2


load_dotenv()

BOT_TOKEN = os.getenv('token')
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands='start')
async def main_handler(msg: types.Message):
    # await msg.answer(f"Assalomu alaykum -> {msg.from_user.id}")
    design1 = [
        ['⬅️Asosiy menu']
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design1 , resize_keyboard=True)
    await msg.answer("-----------------------",reply_markup=rkm)

    design = [
        [InlineKeyboardButton('Menu', callback_data='7')],
        [InlineKeyboardButton('🛒Buyurtma berish', callback_data='1'),InlineKeyboardButton('ℹ️Biz haqimizda', callback_data='2')],
        [InlineKeyboardButton('🛍Buyurtmalarim', callback_data='3')],
        [InlineKeyboardButton('🏠Filiallar', callback_data='4'),InlineKeyboardButton('📝Fikr bildirish ', callback_data='5')],
        [InlineKeyboardButton('⚙️Sozlamalar', callback_data='6')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await msg.answer("Assalomu alaykum Oqtepa botining kloniga xush kelibsiz!!! Davom etish uchun pastdagi buyruqlardan birini tanlang: ", reply_markup=ikm)


@dp.message_handler(Text('⬅️Asosiy menu'))
async def back_handler(msg:types.Message):

    design = [
        [InlineKeyboardButton('Menu', callback_data='7')],
        [InlineKeyboardButton('🛒Buyurtma berish', callback_data='1'),
         InlineKeyboardButton('ℹ️Biz haqimizda', callback_data='2')],
        [InlineKeyboardButton('🛍Buyurtmalarim', callback_data='3')],
        [InlineKeyboardButton('🏠Filiallar', callback_data='4'),
         InlineKeyboardButton('📝Fikr bildirish ', callback_data='5')],
        [InlineKeyboardButton('⚙️Sozlamalar', callback_data='6')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await msg.answer("Assalomu alaykum Oqtepa botining kloniga xush kelibsiz!!! Davom etish uchun pastdagi buyruqlardan birini tanlang: ",reply_markup=ikm)
    await msg.delete()


@dp.callback_query_handler(Text('1'))
async def callback_handler1(callback : types.CallbackQuery):
    design1 = [
        ['🛵Eltib berish', '🚶Borib olish'],
        ['⬅️Asosiy menu']
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design1, resize_keyboard=True)
    await callback.message.answer("-----------------------", reply_markup=rkm)
    await callback.message.delete()

    design = [
        [InlineKeyboardButton('🌯Lavashlar', callback_data='a'),InlineKeyboardButton('🌭Hot Doglar', callback_data='b')],
        [InlineKeyboardButton('🥤Ichimliklar', callback_data='c'),InlineKeyboardButton('🥗Salatlar', callback_data='d')],
        [InlineKeyboardButton('⬅️Ortga', callback_data='or')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("Sizga yoqadigan mahsulotlarning barchasi bizda bor: ",reply_markup=ikm)
    await callback.message.delete()

# -----------------------------------------------------------------

@dp.callback_query_handler(Text('a'))
async def callback_handler11(callback : types.CallbackQuery):
    design = [
        [InlineKeyboardButton('Orginal lavash',callback_data='o'), InlineKeyboardButton('Pishloqli lavash',callback_data='p')],
        [InlineKeyboardButton('⬅️Ortga', callback_data='or')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("Sizga yoqadigan lavashlar bizda bor",reply_markup=ikm)
    await callback.message.delete()

@dp.callback_query_handler(Text('b'))
async def callback_handler11(callback : types.CallbackQuery):
    design = [
        [InlineKeyboardButton('Hot-dog',callback_data='h'), InlineKeyboardButton('Pishloqli Hot-dog',callback_data='t')],
        [InlineKeyboardButton('⬅️Ortga', callback_data='or')]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("Sizga yoqadigan hot-doglar bizda bor",reply_markup=ikm)
    await callback.message.delete()

@dp.callback_query_handler(Text('c'))
async def callback_handler11(callback : types.CallbackQuery):
    design = [
        [InlineKeyboardButton('Coca Cola',callback_data='l'), InlineKeyboardButton('Pepsi',callback_data='s')],
        [InlineKeyboardButton('⬅️Ortga', callback_data='or')]

    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("Sizga yoqadigan ichimliklar bizda bor",reply_markup=ikm)
    await callback.message.delete()

@dp.callback_query_handler(Text('d'))
async def callback_handler11(callback : types.CallbackQuery):
    design = [
        [InlineKeyboardButton('Mujskoy kapriz',callback_data='m'), InlineKeyboardButton('Sezar',callback_data='z')],
        [InlineKeyboardButton('⬅️Ortga', callback_data='or')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("Sizga yoqadigan salatlar bizda bor",reply_markup=ikm)
    await callback.message.delete()



@dp.callback_query_handler(Text('or'))
async def callback_handler1(callback : types.CallbackQuery):
    design = [
        [InlineKeyboardButton('🌯Lavashlar', callback_data='a'),InlineKeyboardButton('🌭Hot Doglar', callback_data='b')],
        [InlineKeyboardButton('🥤Ichimliklar', callback_data='c'),InlineKeyboardButton('🥗Salatlar', callback_data='d')],
        [InlineKeyboardButton('⬅️Ortga',callback_data='ort')]
           ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("Sizga yoqadigan mahsulotlarning barchasi bizda bor: ",reply_markup=ikm)
    await callback.message.delete()


# ------------------------------------------------------------------



@dp.callback_query_handler(Text('2'))
async def callback_handler2(callback : types.CallbackQuery):

    await callback.message.answer("Mening birinchi yaratgan klonim ")
    await callback.message.delete()

    design = [
        [InlineKeyboardButton('⬅️Ortga', callback_data='ort')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("-", reply_markup=ikm)



@dp.callback_query_handler(Text('3'))
async def callback_handler3(callback : types.CallbackQuery):
    await callback.message.answer("""
    Sizning buyurtmalaringiz:
            Lavash🌯: 2 ta
            Hot Dog🌭: 3 ta
            Ichimlik🥤: 1L Cola
    """)

    design = [
        [InlineKeyboardButton('⬅️Ortga', callback_data='ort')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("-",reply_markup=ikm)
    await callback.message.delete()





@dp.callback_query_handler(Text('4'))
async def callback_handler4(callback : types.CallbackQuery):

    design = [
        [InlineKeyboardButton('Algoritm',callback_data='A'), InlineKeyboardButton('Beruniy',callback_data='B')],
        [InlineKeyboardButton('Chilonzor metro',callback_data='CH'), InlineKeyboardButton('Bodomzor',callback_data='Z')],
        [InlineKeyboardButton('⬅️Ortga', callback_data='ort')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("Filiallarimiz bilan tanshing:",reply_markup=ikm)
    await callback.message.delete()

# -----------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(Text('A'))
async def callback_handler11(callback : types.CallbackQuery):
    await callback.message.answer("Ташкент, Чиланзарский район, махалля Бахористон махалля Бахористон (http://maps.yandex.ru/?text=41.262952,69.161994) 🕑 10:00-02:40")
    await callback.message.delete()

@dp.callback_query_handler(Text('B'))
async def callback_handler11(callback : types.CallbackQuery):
    await callback.message.answer(" Ташкент, улица Беруни, 47  (http://maps.yandex.ru/?text=41.344468,69.205111) 🕑 10:00-22:00")
    await callback.message.delete()

@dp.callback_query_handler(Text('CH'))
async def callback_handler11(callback : types.CallbackQuery):
    await callback.message.answer(" Ташкент, Чиланзарский район, массив Чиланзор, 16-й квартал, 18  (http://maps.yandex.ru/?text=41.272545,69.202428) 🕑 10:00-02:40")
    await callback.message.delete()

@dp.callback_query_handler(Text('Z'))
async def callback_handler11(callback : types.CallbackQuery):
    await callback.message.answer(" Ташкент, проспект Амира Темура, 98  (http://maps.yandex.ru/?text=41.337487,69.285620) 🕑 10:00-02:40")
    await callback.message.delete()

# --------------------------------------------------------------------------------------------------------------------------

@dp.callback_query_handler(Text('5'))
async def callback_handler5(callback: types.CallbackQuery):
    await callback.message.answer("Fikringizni yozib qoldiring: ")
    await callback.message.delete()

    design = [
           [InlineKeyboardButton('⬅️Ortga', callback_data='ort')]
       ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("-", reply_markup=ikm)


@dp.callback_query_handler(Text('6'))
async def callback_handler6(callback: types.CallbackQuery):

    await callback.message.answer("Hozircha sozlamalr bilan tanishishning imkoni yoq")
    await callback.message.delete()

    design = [
        [InlineKeyboardButton('⬅️Ortga', callback_data='ort')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("-", reply_markup=ikm)


@dp.callback_query_handler(Text('7'))
async def callback_handler1(callback : types.CallbackQuery):
    design = [
        [InlineKeyboardButton('🌯Lavashlar', callback_data='a'),InlineKeyboardButton('🌭Hot Doglar', callback_data='b')],
        [InlineKeyboardButton('🥤Ichimliklar', callback_data='c'),InlineKeyboardButton('🥗Salatlar', callback_data='d')],
        [InlineKeyboardButton('⬅️Ortga',callback_data='ort')]
           ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer("Sizga yoqadigan mahsulotlarning barchasi bizda bor: ",reply_markup=ikm)
    await callback.message.delete()

@dp.callback_query_handler(Text('ort'))
async def callback_handler6(callback: types.CallbackQuery):
    design = [
        [InlineKeyboardButton('Menu', callback_data='7')],
        [InlineKeyboardButton('🛒Buyurtma berish', callback_data='1'),
         InlineKeyboardButton('ℹ️Biz haqimizda', callback_data='2')],
        [InlineKeyboardButton('🛍Buyurtmalarim', callback_data='3')],
        [InlineKeyboardButton('🏠Filiallar', callback_data='4'),
         InlineKeyboardButton('📝Fikr bildirish ', callback_data='5')],
        [InlineKeyboardButton('⚙️Sozlamalar', callback_data='6')]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await callback.message.answer('-',reply_markup=ikm)
    await callback.message.delete()





# @dp.message_handler(commands='start')
# async def main_handler(msg: types.Message, state : FSMContext):
#     design = [
#         ['Login1️⃣', 'Register2️⃣']
#     ]
#     await state.set_state('step1')
#     rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
#     await msg.answer("Assalomu alaykum", reply_markup=rkm)
#
#
# @dp.message_handler(state = "step1")
# async def button1_handler(msg: types.Message):
#     await msg.answer(f"{msg.text} bosildi")
#
#
# @dp.callback_query_handler(Text('1'), state = 'step1')
# async def callback_handler(call: types.CallbackQuery , state : FSMContext):
#     pass



















# @dp.message_handler(Text('button 1️⃣'))
# async def button1_handler(msg: types.Message):
#     ikm = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('inline 1️⃣', callback_data='1_')]])
#
#     await msg.answer("button 1️⃣ bosildi", reply_markup=ikm)
#
#
# @dp.message_handler(lambda msg: msg.text == "button 2️⃣")
# async def button2_handler(msg: types.Message):
#     ikm = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton('inline 2️⃣', callback_data='2')]])
#
#     await msg.answer("button 2️⃣ bosildi", reply_markup=ikm)
#
# @dp.callback_query_handler(Text('1_'))
# async def callback_handler1(callback : types.CallbackQuery):
#     await callback.answer('inline 1 bosildi')
#
# @dp.callback_query_handler(Text('2'))
# async def callback_handler2(callback : types.CallbackQuery):
#     await callback.message.answer(code('inline 2 bosildi') , parse_mode='MarkdownV2')






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

































