from vkbottle import Bot
from src import bps

import os


TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)

for bp in bps:
    bp.load(bot)

bot.run_forever()
