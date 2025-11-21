from telebot import types, TeleBot
from random import randint

bot = TeleBot(<token>)

quests = [
    'Вынеси пакет мусора в большую урну',
    'Сдай батарейки в специальный пункт приема',
    'Используй многоразовую бутылку для воды вместо пластиковой',
    'Откажись от одноразовых приборов для еды',
    'Пройдись пешком вместо поездки на короткие расстояния',
    'Прочитай статью об экологии',
    'Откажись от одноразового стаканчика для напитка',
    'Расскажи другу о своей эко-привычке',
    'Посади комнатное растение',
    'Повторно используй коробку или упаковку',
    'Сортируй мусор сегодня',
    'Когда будешь купаться в озере летом, наведи порядок на берегу, убрав там мусор']

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'''👋 <b>Здравствуй,</b> <em>{message.from_user.first_name}!</em>
<b>Добро пожаловать!</b> Этот бот будет задавать вам задания с целью уменьшить эколгическую проблему в мире. Напиши команду "quest", чтобы уже начать очищать мир от мусора! Если тебе что-то не понятно веди "/help"''', parse_mode='html')
    
@bot.message_handler(commands=['quest'])
def quest(message):
    rq = quests[randint(0, len(quests)-1)]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('✅', callback_data='quest1'))
    bot.send_message(message.chat.id, rq, reply_markup=markup)
    
@bot.callback_query_handler(func=lambda callback: True)
def quest1(callback):
    if callback.data == 'quest1':
        rq = quests[randint(0, len(quests)-1)]
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('✅', callback_data='quest1'))
        bot.send_message(callback.message.chat.id, rq, reply_markup=markup)
        
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '''📄 <b>Вот команды, которые обрабатывает этот бот:</b>

"/start" — Запуск бота;
"/quest" — Запуск подбора заданий;
"/help" — Вывод списка команд.''', parse_mode='html')

bot.polling(none_stop=True)

