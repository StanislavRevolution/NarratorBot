from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

from text_of_answers import text_responses

from config import TOKEN, STICKER_FILE, SCHOOL_PHOTO, SELFIE_PHOTO

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message)
    print(message.from_user.first_name)
    kb = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('Фотки', callback_data='my_photos')
    b2 = InlineKeyboardButton('Хобби', callback_data='my_hobbies')
    b3 = InlineKeyboardButton('Голосовые', callback_data='my_voices')
    b4 = InlineKeyboardButton('GitHub', callback_data='github')
    kb.add(b1, b2, b3, b4)
    with open(STICKER_FILE, 'rb') as sticker_file:
        await bot.send_sticker(message.chat.id, sticker_file) #config
    await bot.send_message(
        message.chat.id,
        text_responses.welcome,
        reply_markup=kb
    )


@dp.callback_query_handler(text="my_photos")
async def handle_school_photo(call: types.CallbackQuery):
    b1 = InlineKeyboardButton('Фото со школы', callback_data='school_photo')
    b2 = InlineKeyboardButton('Последнее селфи', callback_data='last_photo')
    b3 = InlineKeyboardButton('Назад', callback_data='back')
    button_types = [b1, b2, b3]
    kb = InlineKeyboardMarkup().add(*button_types)
    await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb)
    await call.answer()


@dp.callback_query_handler(text=["school_photo", "school_photo2"])
async def handle_school_photo(call: types.CallbackQuery):
    selfie_button_1 = InlineKeyboardButton('Последнее селфи', callback_data='last_photo2')
    back_button_2 = InlineKeyboardButton('Назад', callback_data='delete_last_message')
    with open(SCHOOL_PHOTO, "rb") as photo_file:
        if call.data == "school_photo":
            await bot.send_photo(
                call.message.chat.id,
                photo_file,
                reply_markup=InlineKeyboardMarkup().add(selfie_button_1, back_button_2)
            )
        elif call.data == "school_photo2":
            media = types.InputMediaPhoto(media=photo_file)
            await bot.edit_message_media(
                media,
                call.message.chat.id,
                call.message.message_id,
                reply_markup=InlineKeyboardMarkup().add(selfie_button_1, back_button_2)
            )
        await call.answer()


@dp.callback_query_handler(text=["last_photo", "last_photo2"])
async def handle_last_photo(call: types.CallbackQuery):
    school_button_1 = InlineKeyboardButton('Фото со школы', callback_data='school_photo2')
    back_button_2 = InlineKeyboardButton('Назад', callback_data='delete_last_message')
    with open(SELFIE_PHOTO, "rb") as photo_file:
        if call.data == "last_photo":
            await bot.send_photo(
                call.message.chat.id,
                photo_file,
                reply_markup=InlineKeyboardMarkup().add(school_button_1, back_button_2)
            )
        elif call.data == "last_photo2":
            media = types.InputMediaPhoto(media=photo_file)
            await bot.edit_message_media(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                media=media,
                reply_markup=InlineKeyboardMarkup().add(school_button_1, back_button_2)
            )
        await call.answer()


@dp.callback_query_handler(text="delete_last_message")
async def handle_back_button(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await call.answer()


@dp.callback_query_handler(text="my_hobbies")
async def handle_school_photo(call: types.CallbackQuery):
    b1 = InlineKeyboardButton('Назад', callback_data='back')
    kb = InlineKeyboardMarkup().add(b1)
    await bot.edit_message_text(
        text_responses.about_hobby,
        call.message.chat.id, message_id=call.message.message_id, reply_markup=kb
    )
    await call.answer()


@dp.callback_query_handler(text="back")
async def handle_last_photo(call: types.CallbackQuery):
    kb = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('Фотки', callback_data='my_photos')
    b2 = InlineKeyboardButton('Хобби', callback_data='my_hobbies')
    b3 = InlineKeyboardButton('Голосовые', callback_data='my_voices')
    b4 = InlineKeyboardButton('GitHub', callback_data='github')
    kb.add(b1, b2, b3, b4)
    await bot.edit_message_text(
        text_responses.main_process_text,
        call.message.chat.id,
        call.message.message_id,
        reply_markup=kb
    )
    await call.answer()


@dp.callback_query_handler(text="my_voices")
async def handle_school_photo(call: types.CallbackQuery):
    b1 = InlineKeyboardButton('Все о GPT', callback_data='send_voice:gpt.mp3')
    b2 = InlineKeyboardButton('SQL VS NoSQL', callback_data='send_voice:sql.mp3')
    b3 = InlineKeyboardButton('Первая любовь', callback_data='send_voice:my_love.mp3')
    b4 = InlineKeyboardButton('Назад', callback_data='back')
    kb = InlineKeyboardMarkup().add(b1, b2, b3, b4)
    await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb)
    await call.answer()


@dp.callback_query_handler(text="github")
async def handle_school_photo(call: types.CallbackQuery):
    kb = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton('Удалить сообщение', callback_data='delete_last_message')
    kb.add(b1)
    await bot.send_message(call.message.chat.id, text_responses.github, reply_markup=kb)
    await call.answer()


@dp.callback_query_handler(text_contains='send_voice:')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("send_voice:"):
        filename = call.data[call.data.rfind(':') + 1:]
        with open(f'./demo-media/ogg/{filename}', mode='rb') as file:
            binary_content = file.read()
            await bot.send_voice(call.message.chat.id, binary_content)
            await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp)
