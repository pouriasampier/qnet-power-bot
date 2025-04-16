import telebot
import datetime
import schedule
import time

TOKEN = "7630814415:AAEmhlxhU3yrZgKOjDtmatQmG_vlE9tswBY"
CHAT_ID = 810616751
bot = telebot.TeleBot(TOKEN)

motivational_messages = [
    "موفقیت تصادفی نیست، تلاش مستمر می‌خواهد!",
    "اگه می‌خوای به چیزی برسی، باید بیشتر از بقیه بخوایش!",
    "هر روز یه قدم کوچیک، یه موفقیت بزرگ می‌سازه.",
    "باور کن می‌تونی، چون واقعاً می‌تونی!"
]

def send_motivation():
    now = datetime.datetime.now()
    message = motivational_messages[now.day % len(motivational_messages)]
    bot.send_message(CHAT_ID, message)

schedule.every().day.at("09:00").do(send_motivation)

while True:
    schedule.run_pending()
    time.sleep(60)