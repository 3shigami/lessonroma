from aiogram import types
from database import Database

class Markup_janre:

    def get_markup():
        markup = types.InlineKeyboardMarkup(row_width=1)
        for i in Database.get_janre():
            markup.add(types.InlineKeyboardButton(i[0], callback_data=i[0]))

        return markup
