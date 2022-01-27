from vkbottle import Bot
from src import app, bps, TOKEN
from multiprocessing import Process


def start_bot():
    bot = Bot(token=TOKEN)

    for bp in bps:
        bp.load(bot)

    bot.run_forever()


def start_api():
    import uvicorn
    uvicorn.run(app, host='0.0.0.0')


if __name__ == '__main__':
    Process(target=start_bot).start()
    Process(target=start_api).start()
