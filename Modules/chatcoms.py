from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG
from msgs import *
import random 
import twitchio
if not DEBUG:
    ic.disable() 
    
class ChatComs(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ['сообщения'])
    async def msgs(self,ctx:commands.Context, user:twitchio.User = None):
        if user is None:
                count = self.cursor.execute(MSGCOUNTSEL.format(
                                            ID = ctx.author.id, 
                                            CHNL =ctx.channel.name)).fetchone()[0]
                await ctx.send(MSGCOUNTSEN.format(
                                AUTHOR =ctx.author.name,
                                CNT = count,
                                CHNL = ctx.channel.name))
                ic("MSGSA")
        else:
                count = self.cursor.execute(MSGCOUNTSEL.format(
                                            ID = user.id,
                                            CHNL = ctx.channel.name)).fetchone()[0]
                await ctx.send(
                MSGCOUNTSENU.format(
                     AUTHOR = ctx.author.name, 
                     USER = user.name, 
                     CNT = count, 
                     CHNL = ctx.channel.name))
                ic("MSGSU")
        ic()
    @commands.command(aliases = ['длина'])
    async def length(self, ctx):
        random.seed()
        length = random.randint(1,35)
        if ctx.author.name.lower() == "via___0":
            length = 999
        if length < 10:
            await ctx.send(LEN10.format(
                 AUTHOR = ctx.author.name,
                 LNG = length
            ))
            ic("LEN10")
        elif length < 20:
            await ctx.send(LEN20.format(
                 AUTHOR = ctx.author.name,
                 LNG = length
            ))
            ic("LEN20")
        elif length < 28:
            await ctx.send(LEN30.format(
                 AUTHOR = ctx.author.name,
                 LNG = length
            ))
            ic("LEN30")
        elif length < 35:
           await ctx.send(LEN40.format(
                 AUTHOR = ctx.author.name,
                 LNG = length
            ))
           ic("LEN40")
        elif length == 999:
            await ctx.send(LENV.format(
                    AUTHOR = ctx.author.name,
                    LNG = length
                ))
            ic("LENV")
        ic()
def prepare(client):
    client.add_cog(ChatComs(client))