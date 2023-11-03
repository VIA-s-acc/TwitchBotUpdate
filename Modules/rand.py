from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG
from msgs import *
import random
import randfacts
import pyjokes
from quote import quote
from googletrans import Translator
import time

if not DEBUG:
    ic.disable() 
    
class Rand(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ['факт'])
    async def randfact(self, ctx):
        fact = randfacts.get_fact(False)
        fact_send = Translator().translate(text = str(fact), src = 'en', dest='ru')
        await ctx.send(f'РАНДОМНЫЙ ФАКТ:    {fact_send.text}')
        ic()
    
    @commands.command(aliases = ['шутка'])
    async def randjoke(self,ctx:commands.Context):
        joke = pyjokes.get_joke(category='all')
        joke_send = Translator().translate(text = str(joke), src = 'en', dest='ru')
        await ctx.send(f'РАНДОМНАЯ ШУТКА:    {joke_send.text}')
        ic()
    
    @commands.command(aliases = ['цитата'])
    async def randquote(self, ctx, name = 'family'):
        quotes = quote(name)
        random.seed()
        try:
            a = len(quotes)
            pass
        except Exception as e:
            await ctx.send(RQUOTERRMSG.format(
                            AUTHOR = ctx.author.name,
                            NAME = name
                        ))
            ic("RQOUTERR")
            return

        quote_no = random.randint(0, len(quotes)-1)
        quotes_send = Translator().translate(text = str(quotes[quote_no]['quote']), dest='ru')
        timeout = time.time() + 10
        ic("RQSTART")
        while len(f"РАНДОМНАЯ ЦИТАТА :    {quotes_send.text} | Автор : {quotes[quote_no]['author']} | Книга : {quotes[quote_no]['book']}.") >= 500:
            if time.time() > timeout:
                await ctx.send(RQUOTEGENERRMSG.format(
                    AUTHOR = ctx.author.name, 
                    NAME = name
                ))
                return
            ic("RQTIMEOUT")
            try:
                quote_no = random.randint(0, len(quotes)-1)
                quotes_send = Translator().translate(text = str(quotes[quote_no]['quote']), dest='ru')
                ic("RQTRANSLATOR")
            except: pass
        if len(quotes[quote_no]['book']) != 0:
            await ctx.send(RQUOTEMSGF.format(
                            TEXT = quotes_send.text,
                            AUTHOR = quotes[quote_no]['author'],
                            BOOK = quotes[quote_no]['book']
                        ))
            ic("RQ1")
        else:
            await ctx.send(RQUOTEMSGS.format(
                TEXT = quotes_send.text,
                AUTHOR = quotes[quote_no]['author']
            ))
            ic('RQ2')
        ic()

def prepare(client):
    client.add_cog(Rand(client))