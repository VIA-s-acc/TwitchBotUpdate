import logging
import os
import sqlite3
from twitchio.ext import commands
from icecream import ic
from config import *
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)  
else:
    logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('TwitchBot')
file_handler = logging.FileHandler('bot_logs.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=cfg["TOKEN"], prefix=DEFAULT_PREFIX, initial_channels=cfg["CHANNELS"])

    



bot = Bot()


for file in os.listdir("./Modules"):
    if file.endswith(".py"):
        bot.load_module(f"Modules.{file[:-3]}")

bot.run()