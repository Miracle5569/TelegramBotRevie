import telebot
import text
import picture
import os
import random
from telebot import types

bot = telebot.TeleBot(text.token)


@bot.message_handler(commands=['start'])
def handlee_text(message):
    key = types.ReplyKeyboardMarkup(True, False)
    key.row("\U0001F646 Рандом арты")
    key.row("\U0000270F Скетчи")
    key.row("\U00002712 Арты художников")
    bot.send_photo(message.chat.id, photo=picture.hello,
                   caption=text.Send_message, reply_markup=key)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "\U0000270F Скетчи":
        key = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="1", callback_data="1")
        btn_2 = types.InlineKeyboardButton(text="2", callback_data="2")
        btn_3 = types.InlineKeyboardButton(text="3", callback_data="3")
        btn_4 = types.InlineKeyboardButton(text="\U000023E9", callback_data="->")
        key.add(btn_1, btn_2, btn_3, btn_4)
        bot.send_message(message.chat.id,
                         text="Здорого, я подготовил для тебя несколько скетчей, выбирай любую из представденных \U0001F60B",
                         reply_markup=key)

    # Рандом арты-----------------------------------------------------------
    if message.text == "\U0001F646 Рандом арты":
        directory = 'Random picture'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_photo(message.chat.id, img)

    # --------------------------------------------------------------------------------------------------------------------------------------------
    # АРТЫ ХУДОЖНИКОВ
    if message.text == "\U00002712 Арты художников":
        key = types.ReplyKeyboardMarkup(True, False)
        key.row("\U0001F467 Olga Lakomaya", "\U0001F469 Александра Ефимова")
        key.row("\U0001F478 Кристина Виверс", "\U0001F468 Александр Викторович")
        key.row("Вернуться назад\U000021A9")
        bot.send_message(
            message.chat.id, text="Выбери интересующего тебе художника\U0000270C", reply_markup=key)

    # НАЗАД В ГЛАВНОЕ МЕНЮ-------------------------------------------------------------------------------------
    if message.text == "Вернуться назад\U000021A9":
        key = types.ReplyKeyboardMarkup(True, False)
        key.row("\U0001F646 Рандом арты", "\U0000270F Скетчи")
        key.row("\U00002712 Арты художников")
        bot.send_message(
            message.chat.id, text="Возращаемся назад к главному меню\U000023F3", reply_markup=key)
    # НАЗАД В ГЛАВНОЕ МЕНЮ-------------------------------------------------------------------------------------

    if message.text == "\U0001F467 Olga Lakomaya":
        key = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="\U00000031\U000020E3", callback_data="Olga1")
        btn_2 = types.InlineKeyboardButton(text="\U00000032\U000020E3", callback_data="Olga2")
        btn_3 = types.InlineKeyboardButton(text="\U00000033\U000020E3", callback_data="Olga3")
        btn_4 = types.InlineKeyboardButton(text="\U00000034\U000020E3", callback_data="Olga4")
        key.add(btn_1, btn_2)
        key.add(btn_3, btn_4)
        bot.send_message(message.chat.id, text="Нажми на одну из цифр и наслаждайся пейзажами\U00002757",
                         reply_markup=key)

    if message.text == "\U0001F469 Александра Ефимова":
        key = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="\U00000031\U000020E3", callback_data="Alexandra1")
        btn_2 = types.InlineKeyboardButton(text="\U00000032\U000020E3", callback_data="Alexandra2")
        btn_3 = types.InlineKeyboardButton(text="\U00000033\U000020E3", callback_data="Alexandra3")
        btn_4 = types.InlineKeyboardButton(text="\U00000034\U000020E3", callback_data="Alexandra4")
        key.add(btn_1, btn_2)
        key.add(btn_3, btn_4)
        bot.send_message(message.chat.id, text="Нажми на одну из цифр и наслаждайся пейзажами\U00002757",
                         reply_markup=key)

    if message.text == "\U0001F478 Кристина Виверс":
        key = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="\U00000031\U000020E3", callback_data="Cristina1")
        btn_2 = types.InlineKeyboardButton(text="\U00000032\U000020E3", callback_data="Cristina2")
        btn_3 = types.InlineKeyboardButton(text="\U00000033\U000020E3", callback_data="Cristina3")
        btn_4 = types.InlineKeyboardButton(text="\U00000034\U000020E3", callback_data="Cristina4")
        key.add(btn_1, btn_2)
        key.add(btn_3, btn_4)
        bot.send_message(message.chat.id, text="Нажми на одну из цифр и наслаждайся пейзажами\U00002757",
                         reply_markup=key)

    if message.text == "\U0001F468 Александр Викторович":
        key = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="\U00000031\U000020E3", callback_data="Alex1")
        btn_2 = types.InlineKeyboardButton(text="\U00000032\U000020E3", callback_data="Alex2")
        btn_3 = types.InlineKeyboardButton(text="\U00000033\U000020E3", callback_data="Alex3")
        btn_4 = types.InlineKeyboardButton(text="\U00000034\U000020E3", callback_data="Alex4")
        key.add(btn_1, btn_2)
        key.add(btn_3, btn_4)
        bot.send_message(message.chat.id, text="Нажми на одну из цифр и наслаждайся пейзажами\U00002757",
                         reply_markup=key)


# --------------------------------------------------------------------------------------------------------------------------------------------


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(message):
    # Обработка кнопки "Скетчи"
    # Копия основного менбю для того что бы можно было вернуться назад
    if message.data == "mainmenu":
        key = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(text="1", callback_data="1")
        btn_2 = types.InlineKeyboardButton(text="2", callback_data="2")
        btn_3 = types.InlineKeyboardButton(text="3", callback_data="3")
        btn_4 = types.InlineKeyboardButton(text="\U000023E9", callback_data="->")
        key.add(btn_1, btn_2, btn_3, btn_4)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="\U0001F64C Здорого, я подготовил для тебя несколько скетчей, выбирай любую из представденных",
                              reply_markup=key)
    # обработка кнопки вперед
    elif message.data == "->":
        key = types.InlineKeyboardMarkup()
        btn_5 = types.InlineKeyboardButton(text="4", callback_data="5")
        btn_6 = types.InlineKeyboardButton(text="5", callback_data="6")
        btn_7 = types.InlineKeyboardButton(text="6", callback_data="7")
        btn_8 = types.InlineKeyboardButton(text="\U000023E9", callback_data="-->")
        btn_back = types.InlineKeyboardButton(
            text="\U000023EA", callback_data="mainmenu")
        key.add(btn_5, btn_6, btn_7, btn_8, btn_back)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="\U0001F64C Здорого, я подготовил для тебя несколько скетчей, выбирай любую из представденных",
                              reply_markup=key)
    # Обработка кнопки вперед (последняя страница)
    elif message.data == "-->":
        key = types.InlineKeyboardMarkup()
        btn_5 = types.InlineKeyboardButton(text="7", callback_data="8")
        btn_6 = types.InlineKeyboardButton(text="8", callback_data="9")
        btn_7 = types.InlineKeyboardButton(text="9", callback_data="10")
        btn_8 = types.InlineKeyboardButton(text="10", callback_data="11")
        btn_back = types.InlineKeyboardButton(
            text="\U000023EA", callback_data="->")
        key.add(btn_5, btn_6, btn_7, btn_8)
        key.add(btn_back)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="\U0001F64C Здорого, я подготовил для тебя несколько скетчей, выбирай любую из представденных",
                              reply_markup=key)

    # Оработка отправки сообщений на нажатие кнопок
    if message.data == "1":
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture,
                       caption=None, reply_markup=key)

    # кнопка удаления на картинке
    if message.data == 'Delete':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Второй скетч
    elif message.data == '2':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete2")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture2,
                       caption=None, reply_markup=key)

    # Удаление второй картинки
    if message.data == 'Delete2':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Третья картинка
    elif message.data == '3':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete3")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture3,
                       caption=None, reply_markup=key)

    # Удаление третьей кратинки
    if message.data == 'Delete3':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Четвертая картинка
    elif message.data == '5':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete4")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture4,
                       caption=None, reply_markup=key)

    # Удаление Четвертой кратинки
    if message.data == 'Delete4':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Пятая картинка
    elif message.data == '6':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete5")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture5,
                       caption=None, reply_markup=key)

    # Удаление Пятой кратинки
    if message.data == 'Delete5':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Шестая картинка
    elif message.data == '7':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete6")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture6,
                       caption=None, reply_markup=key)

    # Удаление Шестая кратинки
    if message.data == 'Delete6':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Седьмая картинка
    elif message.data == '8':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete7")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture7,
                       caption=None, reply_markup=key)

    # Удаление Седьмая кратинки
    if message.data == 'Delete7':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Восьмая картинка
    elif message.data == '9':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete8")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture8,
                       caption=None, reply_markup=key)

    # Удаление Всоьмая кратинки
    if message.data == 'Delete8':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Девятая картинка
    elif message.data == '10':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete9")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture9,
                       caption=None, reply_markup=key)

    # Удаление девятая кратинки
    if message.data == 'Delete9':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Десятая картинка
    elif message.data == '11':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="Delete10")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id, photo=picture.picture10,
                       caption=None, reply_markup=key)

    # Удаление десятая кратинки
    if message.data == 'Delete10':
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)
    # ---------------------------------------------------------------------------------------------------------------------------
    # АРТЫ ХУДОЖНИКОВ
    # Olga Lakomaya----------------------------------------
    if message.data == 'Olga1':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="OlgaDelete")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.OlgaLakomaya, caption=None, reply_markup=key)

    if message.data == "OlgaDelete":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Olga2':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="OlgaDelete2")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.OlgaLakomaya2, caption=None, reply_markup=key)

    if message.data == "OlgaDelete2":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Olga3':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="OlgaDelete3")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.OlgaLakomaya3, caption=None, reply_markup=key)

    if message.data == "OlgaDelete3":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Olga4':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="OlgaDelete4")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.OlgaLakomaya4, caption=None, reply_markup=key)

    if message.data == "OlgaDelete4":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Александра Ефимова--------------------------------

    if message.data == 'Alexandra1':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="AlexandraDelete")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Alexandra, caption=None, reply_markup=key)

    if message.data == "AlexandraDelete":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Alexandra2':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="AlexandraDelete2")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Alexandra2, caption=None, reply_markup=key)

    if message.data == "AlexandraDelete2":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Alexandra3':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="AlexandraDelete3")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Alexandra3, caption=None, reply_markup=key)

    if message.data == "AlexandraDelete3":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Alexandra4':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="AlexandraDelete4")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Alexandra4, caption=None, reply_markup=key)

    if message.data == "AlexandraDelete4":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Кристина Виверс -------------------------------------------
    if message.data == 'Cristina1':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="CristinaDelete")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Cristina, caption=None, reply_markup=key)

    if message.data == "CristinaDelete":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Cristina2':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="CristinaDelete2")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Cristina2, caption=None, reply_markup=key)

    if message.data == "CristinaDelete2":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Cristina3':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="CristinaDelete3")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Cristina3, caption=None, reply_markup=key)

    if message.data == "CristinaDelete3":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Cristina4':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="CristinaDelete4")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Cristina4, caption=None, reply_markup=key)

    if message.data == "CristinaDelete4":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    # Александр Викторович -------------------------------------------
    if message.data == 'Alex1':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="AlexDelete")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Alex, caption=None, reply_markup=key)

    if message.data == "AlexDelete":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Alex2':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="AlexDelete2")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Alex2, caption=None, reply_markup=key)

    if message.data == "AlexDelete2":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Alex3':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="AlexDelete3")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Alex3, caption=None, reply_markup=key)

    if message.data == "AlexDelete3":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)

    if message.data == 'Alex4':
        key = types.InlineKeyboardMarkup()
        btn_delete = types.InlineKeyboardButton(
            text="\U0000274C Delete", callback_data="AlexDelete4")
        key.add(btn_delete)
        bot.send_photo(chat_id=message.message.chat.id,
                       photo=picture.Alex4, caption=None, reply_markup=key)

    if message.data == "AlexDelete4":
        bot.delete_message(chat_id=message.message.chat.id,
                           message_id=message.message.message_id)


bot.polling(none_stop=True, interval=0)
