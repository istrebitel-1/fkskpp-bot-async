from vkbottle import Bot
from src import app, bps, TOKEN, config
from multiprocessing import Process


def start_bot():
    bot = Bot(token=TOKEN)

    for bp in bps:
        bp.load(bot)

    bot.run_forever()


def start_api():
    import uvicorn
    uvicorn.run(app)


if __name__ == '__main__':
    if config['runtime'] == 'DEV':
        Process(target=start_bot).start()
        Process(target=start_api).start()

    elif config['runtime'] == 'PROD':
        start_bot()
