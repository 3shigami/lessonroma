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