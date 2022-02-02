from .blueprints import bps
from .scheduler import do_schedule

from json import load
import os
import dotenv


with open('config.json', 'r', encoding='utf-8') as config_file:
    config = load(config_file)

runtime = config['runtime']

if runtime == 'DEV':
    dotenv.load_dotenv('.env')
    TOKEN = os.environ['TOKEN']

elif runtime == 'PROD':
    TOKEN = os.environ['TOKEN']
