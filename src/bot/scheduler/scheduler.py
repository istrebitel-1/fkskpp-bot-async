import imp
from src.bot.parsers.news import get_news
from vk_api import VkApi
import schedule
import time


def send_new():

    new = get_news()
    msg = f'{new[0]}\n\n{new[1]}\n\n{new[2]}'
    from src.bot import TOKEN
    vk_session = VkApi(token=TOKEN)
    vk = vk_session.get_api()
    vk.messages.send(
        message=msg,
        chat_id=1,
        random_id=0
    )


def do_schedule():
    schedule.every().minute.at(":01").do(send_new)
    while True:
        schedule.run_pending()
        time.sleep(1)
