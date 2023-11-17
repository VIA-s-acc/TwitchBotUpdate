from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG
from msgs import *
import datetime
import asyncio
import twitchio
waiting_users = {}

if not DEBUG:
    ic.disable() 
    
class Marriage(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ['брак'])
    async def marry(self, ctx, user:twitchio.User = None):
        if user != None:
            if self.cursor.execute(SELUSF.format(
                                    USRF = user.id,
                                    CHNL = ctx.channel.name)).fetchone() is not None:
                await ctx.send(INMR.format(AUTHOR = ctx.author.name, USER = user.name))
                ic("INMR")
                return
            if user == ctx.author:
                try:
                    del waiting_users[f"{ctx.channel.name}_{ctx.author}"]
                    del waiting_users[f"{ctx.channel.name}_{user}"] 
                except:pass
                await ctx.send(SELFM.format(AUTHOR = ctx.author.name))
                ic("SELFM")
                return
            try:
                if len(waiting_users[f"{ctx.channel.name}_{user}"]) > 0:
                        await ctx.send(MWAIT.format(
                            AUTHOR = ctx.author.name,
                            USRF = waiting_users[f"{ctx.channel.name}_{user}"][0],
                            USRS = waiting_users[f"{ctx.channel.name}_{user}"][1]))
                        ic("MWAIT")
                        return
            except:pass
            try:
                if len(waiting_users[f"{ctx.channel.name}_{ctx.author}"]) > 0:
                    await ctx.send(MWAIT.format(
                            AUTHOR = ctx.author.name,
                            USRF = waiting_users[f"{ctx.channel.name}_{user}"][0],
                            USRS = waiting_users[f"{ctx.channel.name}_{user}"][1])) 
                    ic("MWAIT")
                    return    
            except:pass
            waiting_users[f"{ctx.channel.name}_{ctx.author}"] = [ctx.author.name,user.name]
            waiting_users[f"{ctx.channel.name}_{user}"] = [ctx.author.name,user.name]
            if self.cursor.execute(SELUSF.format(
                                    USRF = user.id,
                                    CHNL = ctx.channel.name)).fetchone() is None:
                try:
                    await ctx.send(MRANSWMSG.format(AUTHOR = ctx.author.name, USER = user.name))
                    message = await self.client.wait_for("message", timeout=60.0, predicate=lambda message: message.content.lower() == "да" and message.author.name == user.name)
                    if message: 
                                        try:
                                            del waiting_users[f"{ctx.channel.name}_{ctx.author}"]
                                            del waiting_users[f"{ctx.channel.name}_{user}"] 
                                        except:pass
                                        self.cursor.execute("INSERT INTO marry VALUES('{}',{},{},'{}','{}','{}')".format(
                                            ctx.channel.name,
                                            ctx.author.id,
                                            user.id,
                                            ctx.author.name,
                                            user.name,
                                            datetime.datetime.now()
                                        ))
                                        self.cursor.execute("INSERT INTO marry VALUES('{}',{},{},'{}','{}','{}')".format(
                                            ctx.channel.name,
                                            user.id,
                                            ctx.author.id,
                                            user.name,
                                            ctx.author.name,
                                            datetime.datetime.now()
                                        ))
                                        self.connection.commit() 
                                        await ctx.send(f"Поздравим {ctx.author.name} и {user.name} с браком!!! ")
                                        ic('SUCMRG')
                                        return
                except asyncio.TimeoutError:
                    try:
                        del waiting_users[f"{ctx.channel.name}_{ctx.author}"]
                        del waiting_users[f"{ctx.channel.name}_{user}"] 
                    except:pass
                    await ctx.send(f"{ctx.author.name}, Время истекло,  брак с {user.name} не был заключен 😭😭.")
                    ic("TMOUTMRG")
                    return
            else:
                try:
                        del waiting_users[f"{ctx.channel.name}_{ctx.author}"]
                        del waiting_users[f"{ctx.channel.name}_{user}"] 
                except:pass
                await ctx.send(f"{ctx.author.name}, вы уже состоите в браке.")
                ic("INM")
                return
        else:
                await ctx.send(USSELERR.format(AUTHOR= ctx.author.name))
                ic("USSELERR")
                return
        ic()
        
    @commands.command(aliases = ['расторгнуть'])
    async def divorce(self, ctx):
        if self.cursor.execute(SELUSF.format(
                                    USRF = ctx.author.id,
                                    CHNL = ctx.channel.name)).fetchone() is None:
            await ctx.send(MRGNOT.format(
                AUTHOR = ctx.author.name
            ))
            ic("NOMRG")
        else:
            user2_id = self.cursor.execute(SELUSS.format(
                USRF = ctx.author.id,
                CHNL = ctx.channel.name
            )).fetchone()[0]
            user2_name = self.cursor.execute(SELUSSN.format(
                USRF = ctx.author.id,
                CHNL = ctx.channel.name)).fetchone()[0]
            self.cursor.execute(DELFMRS.format(
                USRF = ctx.author.id,
                CHNL = ctx.channel.name))
            self.cursor.execute(DELFMRS.format(
                USRF = user2_id,
                CHNL = ctx.channel.name))
            self.connection.commit()
            await ctx.send(f"Брак между {ctx.author.name} и {user2_name} рассторгнут 😢.")
            ic("MRGDVS")
        ic()

    @commands.command(aliases = ['статус'])
    async def mstatus(self, ctx: commands.Command, User: twitchio.User = None):
        if User is None:
            user = ctx.author
        else:
            user = User
        if self.cursor.execute(SELUSF.format(
                                    USRF = user.id,
                                    CHNL = ctx.channel.name)).fetchone() is None:
            if User is None:
                await ctx.send(MRGNOT.format(
                AUTHOR = ctx.author.name
            ))
                ic("MRGNOT")
            else:
                await ctx.send(UMRGNOT.format(
                    AUTHOR = ctx.author.name,
                    USER = user.name
                ))
                ic("UMRGNOT")
            return
        else:
            user2_name = self.cursor.execute(SELUSSN.format(
                USRF = user.id,
                CHNL = ctx.channel.name)).fetchone()[0]
            date_now = datetime.datetime.now()
            date =  self.cursor.execute("SELECT date FROM marry WHERE user1_id = {} AND channel_name = '{}'".format(user.id,ctx.channel.name)).fetchone()[0]
            date_marry = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
            duration = date_now - date_marry 
            duration_in_s = duration.total_seconds() 
            days    = divmod(duration_in_s, 86400)        
            hours   = divmod(days[1], 3600)               
            minutes = divmod(hours[1], 60)               
            seconds = divmod(minutes[1], 1)
            if User is None:
                await ctx.send(f"{ctx.author.name}, вы в браке с {user2_name} уже {days[0]} дней, {hours[0]} часов, {minutes[0]} минут, {seconds[0]} секунд.")
                ic("MSTF")
            else:
                await ctx.send(f"{ctx.author.name}, {user.name} в браке с {user2_name} уже {days[0]} дней, {hours[0]} часов, {minutes[0]} минут, {seconds[0]} секунд.")
                ic("MSTS")
            ic()
            return  
def prepare(client):
    client.add_cog(Marriage(client))