import telebot

bot = telebot.TeleBot('5213963013:AAE1efkfcMCU1p8E8ZdTWJpjFYyXA8262qY')

from worker import Worker

worker = Worker()
print("LETS GOOOOOOOO_____________+")

def pretty_print(tags):
    try:
        string = worker.gen_names(tags)
    except Exception:
        print(Exception)
        return "Ой, что-то пошло не так"
    ans = "Мои рекомендации:"
    for i in range(len(string)):
        ans += "\n" + str(i+1) + '. ' + string[i]
    return ans


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, чтобы понять что я могу напиши /help")
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "Я могу помочь тебе решить с какой книгой провести своё свободное время. \nДля рекомендаций попробуй ввесте /find и список тегов разделённых запятой, а я по ним попробую подобрать книги!")
    elif message.text.startswith('/find'):
        bot.send_message(message.from_user.id, pretty_print(message.text[5:]))
    else:
        bot.send_message(message.from_user.id, "На этом мой функционал всио")


bot.polling(none_stop=True, interval=0)
