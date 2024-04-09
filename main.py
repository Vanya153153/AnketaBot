import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
from Users import user_data, file_user_id
import json
from Questions import qu
import telebot
import time
from peremen import *




# Создаём бота

bot = telebot.TeleBot(API_TOKEN)

#счётчик ответов



markup = ReplyKeyboardMarkup(resize_keyboard=True) # заготовка для клавиатуры
markup.add(KeyboardButton('/start'))
markup.add(KeyboardButton('/help'))
markup.add(KeyboardButton('/start_anket'))



@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Приветствую! Я бот-анкета на тему "Какой тип подарка на новый год тебе подойдёт ?"', reply_markup=markup)
    bot.send_message(message.chat.id, 'Что-бы начать используй команду "start_anket", или посмотри что могу через комманду "help"', reply_markup=markup)
    user_id = message.from_user.id
    user_nm = message.from_user.first_name
    file_user_id(user_nm, user_id)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Я бот-анкета вычесляющий какой тип подарка тебе больше всего подойдёт\n"
                     "Вот мои комманды: \n"
                     "/start: Комманда запускающая меня.\n"
                     "/help: Комманда показывающая что я могу.\n"
                     "/start_anket: Комманда запускающая анкету.")


def que(message, n):
    bot.send_message(message.chat.id, qu[n]["question"])
    for i in qu[n]["answers"]:
        bot.send_message(message.chat.id, i)
    mesg = bot.send_message(message.chat.id, 'Выберете один вариант ответа(1 или 2 и т.д.)')
l = 0
@bot.message_handler(commands=['start_anket'])
def save_age(message):
    bot.send_message(message.chat.id, "Начинаю анкету: ")
    time.sleep(2)
    que(message, 0)
    bot.register_next_step_handler(message, answ1)


#варианты вопросов
def answ1(message):
    if message.text == "1":
        for i, j in qu[0]['answers']["1) Женский"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 1)
        bot.register_next_step_handler(message, answ2)


    elif message.text == "2":
        for i, j in qu[0]['answers']["2) Мужской"].items():
            scors[i] += j

        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 1)
        bot.register_next_step_handler(message, answ2)

    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ2(message):
    global scors
    if message.text == "1":
        for i, j in qu[1]['answers']["1) 0-12"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 2)
        bot.register_next_step_handler(message, answ3)
    elif message.text == "2":
        for i, j in qu[1]['answers']["2) 13-18"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 2)
        bot.register_next_step_handler(message, answ3)
    elif message.text == "3":
        for i, j in qu[1]['answers']["3) 18-30"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 2)
        bot.register_next_step_handler(message, answ3)
    elif message.text == "4":
        for i, j in qu[1]['answers']["4) 31-?"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 2)
        bot.register_next_step_handler(message, answ3)
    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ3(message):
    global scors
    if message.text == "1":
        for i, j in qu[2]['answers']["1) Играть в настольные игры или видеоигры"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 3)
        bot.register_next_step_handler(message, answ4)
    elif message.text == "2":
        for i, j in qu[2]['answers']["2) Отдыхать на воздухе"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 3)
        bot.register_next_step_handler(message, answ4)
    elif message.text == "3":
        for i, j in qu[2]['answers']["3) Активный отдых"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 3)
        bot.register_next_step_handler(message, answ4)
    elif message.text == "4":
        for i, j in qu[2]['answers']["4) Шоппинг"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 3)
        bot.register_next_step_handler(message, answ4)
    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ4(message):
    global scors
    if message.text == "1":
        for i, j in qu[3]['answers']["1) Дома"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 4)
        bot.register_next_step_handler(message, answ5)
    elif message.text == "2":
        for i, j in qu[3]['answers']["2) Тусить(Клуб и т.д.)"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 4)
        bot.register_next_step_handler(message, answ5)
    elif message.text == "3":
        for i, j in qu[3]['answers']["3) В магазине"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 4)
        bot.register_next_step_handler(message, answ5)
    elif message.text == "4":
        for i, j in qu[3]['answers']["4) У друзей"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 4)
        bot.register_next_step_handler(message, answ5)
    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ5(message):
    global scors
    if message.text == "1":
        for i, j in qu[4]['answers']["1) Экстроверт"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 5)
        bot.register_next_step_handler(message, answ6)

    elif message.text == "2":
        for i, j in qu[4]['answers']["2) Интроверт"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 5)
        bot.register_next_step_handler(message, answ6)
    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ6(message):
    global scors
    if message.text == "1":
        for i, j in qu[5]['answers']["1) Да"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 6)
        bot.register_next_step_handler(message, answ7)

    elif message.text == "2":
        for i, j in qu[5]['answers']["2) Нет"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 6)
        bot.register_next_step_handler(message, answ7)
    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ7(message):
    global scors
    if message.text == "1":
        for i, j in qu[6]['answers']["1) Да"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 7)
        bot.register_next_step_handler(message, answ8)

    elif message.text == "2":
        for i, j in qu[6]['answers']["2) Нет"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 7)
        bot.register_next_step_handler(message, answ8)
    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ8(message):
    global scors
    if message.text == "1":
        for i, j in qu[7]['answers']["1) Компьютер"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 8)
        bot.register_next_step_handler(message, answ9)
    elif message.text == "2":
        for i, j in qu[7]['answers']["2) Стол"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 8)
        bot.register_next_step_handler(message, answ9)
    elif message.text == "3":
        for i, j in qu[7]['answers']["3) Духи"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 8)
        bot.register_next_step_handler(message, answ9)
    elif message.text == "4":
        for i, j in qu[7]['answers']["4) Сертификат на посещение чего-либо"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 8)
        bot.register_next_step_handler(message, answ9)
    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ9(message):
    global scors
    if message.text == "1":
        for i, j in qu[8]['answers']["1) Да"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 9)
        bot.register_next_step_handler(message, answ10)

    elif message.text == "2":
        for i, j in qu[8]['answers']["1) Да"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, двигаемся дальше")
        time.sleep(2)
        que(message, 9)
        bot.register_next_step_handler(message, answ10)
    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")

def answ10(message):
    global scors
    if message.text == "1":
        for i, j in qu[9]['answers']["1) Да"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, смотрю на результат...")
        time.sleep(2)

    elif message.text == "2":
        for i, j in qu[9]['answers']["1) Да"].items():
            scors[i] += j
        bot.send_message(message.chat.id, "Ответ принят, смотрю на результат...")
        time.sleep(2)

    elif message.text == "/start_anket" or message.text == "/help" or message.text == "/start":
        bot.send_message(message.chat.id, "Нажмите на комманду ещё раз")
    else:
        bot.send_message(message.chat.id, f"Вы ввели что-то не то ")
    a = 0
    for i, j in scors.items():
        a += j
    if max(scors) == "Техника":
        img = open('тех.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Ваш результат: Вы больше всего хотите технику({a % scors[max(scors)]})")
    elif max(scors) == "Косметика":
        img = open('космет.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Ваш результат: Вы больше всего хотите технику({a % scors[max(scors)]})")
    elif max(scors) == "Мебель":
        img = open('мебель.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Ваш результат: Вы больше всего хотите технику({a % scors[max(scors)]})")
    elif max(scors) == "Игрушка":
        img = open('игр.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Ваш результат: Вы больше всего хотите технику({a % scors[max(scors)]}))")
    elif max(scors) == "Книги":
        img = open('книга.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Ваш результат: Вы больше всего хотите технику({a % scors[max(scors)]}))")
    elif max(scors) == "Спортивный инвентарь":
        img = open('спорт.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Ваш результат: Вы больше всего хотите технику({a % scors[max(scors)]}))")
    else:
        img = open('серт.png', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Ваш результат: Вы больше всего хотите технику({a % scors[max(scors)]}))")

@bot.message_handler(content_types=['text'])
def say_hello(message):
    bot.send_message(message.chat.id, "Здравствуйте ! Я пока не знаю что вы хотите сказать мне, но вы можете вызвать комманду start")


bot.polling(none_stop=True)