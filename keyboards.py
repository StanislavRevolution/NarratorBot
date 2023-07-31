from aiogram.types import InlineKeyboardButton

b1 = InlineKeyboardButton('Фото со школы', callback_data='school_photo')
b2 = InlineKeyboardButton('Последнее селфи', callback_data='last_photo')
b3 = InlineKeyboardButton('Назад', callback_data='back')

back_button_2 = InlineKeyboardButton('Назад', callback_data='delete_last_message')

bu1 = InlineKeyboardButton('Фотки', callback_data='my_photos')
bu2 = InlineKeyboardButton('Хобби', callback_data='my_hobbies')
bu3 = InlineKeyboardButton('Голосовые', callback_data='my_voices')

b1 = InlineKeyboardButton('Все о GPT', callback_data='send_voice:gpt.mp3')
b2 = InlineKeyboardButton('SQL VS NoSQL', callback_data='send_voice:sql.mp3')
b3 = InlineKeyboardButton('Первая любовь', callback_data='send_voice:my_love.mp3')

selfie_button_1 = InlineKeyboardButton('Последнее селфи', callback_data='last_photo2')
school_button_1 = InlineKeyboardButton('Фото со школы', callback_data='school_photo2')
ph_bt_types = [selfie_button_1, school_button_1, back_button_2]

