from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG
from msgs import *
import datetime
from bs4 import BeautifulSoup
import requests

if not DEBUG:
    ic.disable() 

class HoroscopeCog(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ["гороскоп"])
    async def horoscope(self, ctx, sign, day = "сегодня"):
        dic={'овен':'Aries','телец':'Taurus','близнецы':'Gemini',
         'рак':'Cancer','лев':'Leo','дева':'Virgo','весы':'Libra',
         'скорпион':'Scorpio','стрелец':'Sagittarius','козерог':'Capricorn',
         'водолей':'Aquarius','рыбы':'Pisces'} 
        try:
            Sign = dic[sign.lower()].lower()
        except:
            await ctx.send(f"{ctx.author.name}, Введён неприавльный знак зодиака {sign}")
            return
        if day.lower() == "сегодня":
                Day = ''
        elif day.lower() == "завтра":
                Day = 'tomorrow'
        elif day.lower() == "вчера":
                Day = 'yesterday'
        else:
                await ctx.send(f"{ctx.author.name}, Введён неприавльный день {day}")
                return
        url = (
            f"https://horoscopes.rambler.ru/{Sign}/{Day}")
        soup = BeautifulSoup(requests.get(url).content,
                         "html.parser")
        text = soup.find("div", class_="_1E4Zo _3BLIa").p.text
        send = f"{ctx.author.name}, гороскоп на {day.lower()} : "
        await ctx.send(f"{send} {text[:(499-len(send))]}")
        ic()
        
def prepare(client):
    client.add_cog(HoroscopeCog(client))