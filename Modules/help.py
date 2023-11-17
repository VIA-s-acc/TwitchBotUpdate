from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG
from msgs import *
import datetime

if not DEBUG:
    ic.disable() 
    
class help(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ['помощь'])
    async def help(self, ctx, command_name:str=''):
        command_dict = {
            'сообщения': 28,
            'msgs': 28,
            'длина':29,
            'length':29,
            'добком':30,
            'add_comm':30,
            'удлком':30,
            'del_comm':30,
            'гороскоп':31,
            'horoscope':31,
            'info':32,
            'инфо':32,
            'брак':33,
            'marry':33,
            'расторгнуть':34,
            'divorce':34,
            'статус':35,
            'mstatus':35,
            'факт':36,
            'randfact':36,
            'шутка':37,
            'randjoke':37,
            'цитата':38,
            'randquote':38,
            'поиск':39,
            'search':39,
            'погода':40,
            'weather':40,
            'помощь':42,
            'help':42
        }

        command_number = command_dict.get(command_name.lower(), 41)
        if command_number != 41:
            await ctx.send(f'{ctx.author.name}, информация по комманде <{command_name}> доступна в http://viag.pythonanywhere.com/article/{command_number}')
        else:
            await ctx.send(f'{ctx.author.name}, информации по комманде <{command_name}> нет. Посмотрите допступные комманды  в http://viag.pythonanywhere.com/article/41')

        
def prepare(client):
    client.add_cog(help(client))