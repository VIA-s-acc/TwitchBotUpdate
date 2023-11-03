from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG, cfg
from msgs import *
import requests

if not DEBUG:
    ic.disable() 
    
class Weather(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ['погода'])
    async def weather(self, ctx: commands.Context, location):
        API_KEY = cfg["API_KEY"]
        url = WURL.format(
             LCT = location,
             AK = API_KEY
        ) 
        response = requests.get(url)
        data = response.json()
        if data['cod'] == '404':
                await ctx.send(WERRMSG.format(
                     AUTHOR = ctx.author.name
                ))
                ic("WTH404")
                return
        else:
                temp = data['main']['temp'] - 273.15
                await ctx.send(f'Локация : {location}   |   Температура: {temp:.2f}°C.')
                ic("WTHS")
        ic()
        
def prepare(client):
    client.add_cog(Weather(client))