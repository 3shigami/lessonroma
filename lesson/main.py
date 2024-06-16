from aiogram import Bot, executor, Dispatcher, types


"""ание :
Регистрация на мероприятие

Описание которое в чате: 
При помощи этого чат-бота вы можете зарегистрироваться на мероприятие

Функционал: 
/start
Приветственное сообщение
- Здравствуйте, Name! Для регистрации на мероприятие нажмите кнопку регистрация
Кнопка регистрация
Ввод данных имя фамилия возраст
после нажатия на кнопку и ввода данных выводит Вы успешно зарегистрировались 
+ на неизвестное сообщение писать Я не понимаю эту команду или что то такое"""


API_TOKEN = "7456660156:AAE7aZ_N_7VCxbrfIc7R54wEgPY54buKRRA"

#создаем самого бота
bot = Bot(token=API_TOKEN)


dp = Dispatcher(bot)


#создаем событие которое будет отвечать за /start
@dp.message_handler(commands=['start'])
#функция куда попадает сообщение нашего пользователя types.Message - наше сообщение
async def cmd_start(message: types.Message):
    #то что бот будет отвечать на /start
    #любой код
    print(message.chat.id)
    await message.answer("привет")
    #любой код


@dp.message_handler()
async def answer(message: types.Message):
    print(message.text)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



"""1. на /start отвечает привет (мое имя), айди твоего чата - (айди моего чата)
2) на сообщение Привет он отвечал - привет, (мое имя)! чтобы использовать бота нажми /start
3) на сообщение Пока он отвечал - пока"""

















from aiogram import Bot, executor, Dispatcher, types


"""ание :
Регистрация на мероприятие

Описание которое в чате: 
При помощи этого чат-бота вы можете зарегистрироваться на мероприятие

Функционал: 
/start
Приветственное сообщение
- Здравствуйте, Name! Для регистрации на мероприятие нажмите кнопку регистрация
Кнопка регистрация
Ввод данных имя фамилия возраст
после нажатия на кнопку и ввода данных выводит Вы успешно зарегистрировались 
+ на неизвестное сообщение писать Я не понимаю эту команду или что то такое"""


API_TOKEN = "7456660156:AAE7aZ_N_7VCxbrfIc7R54wEgPY54buKRRA"

#создаем самого бота
bot = Bot(token=API_TOKEN)


dp = Dispatcher(bot)


#создаем событие которое будет отвечать за /start
@dp.message_handler(commands=['start'])
#функция куда попадает сообщение нашего пользователя types.Message - наше сообщение
async def cmd_start(message: types.Message):
    #то что бот будет отвечать на /start
    #любой код
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("Медный бык", callback_data="1488"))
    await message.answer("пасхалко", reply_markup=markup)
    #любой код


@dp.message_handler()
async def answer(message: types.Message):
    print(message.text)


@dp.callback_query_handler(text_startswith="1488") 
async def registration(call:types.CallbackQuery):
    print(call)
    """{"id": "4033832339526762352",
      "from": {"id": 939199780, "is_bot": false, "first_name": "eiancbennx", "username": "ehxnekcnejxkexn", "language_code": "ru"},
        "message": {"message_id": 134,
          "from": {"id": 7456660156, "is_bot": true,
            "first_name": "lesson_roma", "username": "lesson_roma_bot"},
              "chat": {"id": 939199780, "first_name": "eiancbennx", "username": "ehxnekcnejxkexn",
                "type": "private"}, "date": 1718588320, "text": "пасхалко",
                  "reply_markup": {"inline_keyboard": [[{"text": "Медный бык", "callback_data": "1488"}]]}},
                    "chat_instance": "7368618751707300189", "data": "1488"}"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("Пасхалко", callback_data="1"))
    await call.message.edit_text("медный бык был нажат", reply_markup=markup)

@dp.callback_query_handler(text_startswith="1") 
async def registration(call:types.CallbackQuery):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("Джокер", callback_data="2"))
    await call.message.edit_text("пасхалко был нажат", reply_markup=markup)


@dp.callback_query_handler(text_startswith="2") 
async def registration(call:types.CallbackQuery):
    await call.message.edit_text("Джоекер был нажат")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


"""1)при /start у человека появляется набор из следующих инлайн кнопок 1)1-10 2)10-15 3)15-20 при сообщении введите ваш возраст, и потом бот редактирует сообщение и пишет, ваш возраст и то что он выбрал"""


