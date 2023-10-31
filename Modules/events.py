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
class EventCog(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.Cog.event("event_ready")
    async def _in_ready(self):
        ic(f'Logged in as | {self.client.nick}')
        ic(f'User id is | {self.client.user_id}')
        ic("TABLE users.")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        user_name INT,
        user_id INT,
        channel_name TEXT,
        message_count INT)""")
        ic("TABLE logs.")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS logs(
    	user_id INT,
    	user_name TEXT,
    	channel_name TEXT,
    	message_text TEXT,
    	date TEXT
        )""")
        ic("TABLE marry.")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS marry(
        channel_name TEXT,
        user1_id INT,
        user2_id INT,
        user1_name TEXT,
        user2_name TEXT,
        date TEXT
        )""")
        ic("TABLE channel.")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS channel(
        channel_name,
        inst TEXT,
        ds TEXT,
        tg TEXT
        )""")
        ic()


    @commands.Cog.event("event_command_error")
    async def _in_command_err(self, ctx, exception):
            if str(exception).lower().startswith("no valid command was passed"):
                return
            if "?" in str(exception):
                return 
            await ctx.send(f"{ctx.author.name}, произошла ошибка при выполнении команды | TBERRMSG : {str(exception)[:450]}")
            ic()

            
    @commands.Cog.event("event_message")
    async def _on_msg(self, message):
        
        if message.echo:
            return

        await self.client.handle_commands(message)
        if self.cursor.execute(IDSELECTMSG.format(
                ID = message.author.id,
                CHNL = message.channel.name
                )).fetchone() is None:
                
                self.cursor.execute(USERINITMSG.format(
                name = message.author.name, 
                id = message.author.id, 
                chnl = message.channel.name, 
                df = 1))
                ic("USERINIT")

        else:
                self.cursor.execute(USERINFUPD.format(
                    COUNT = 1,
                    ID = message.author.id,
                    CHNL = message.channel.name
                ))
        ic(USERUPDMSG.format(
                CHNL = message.channel.name,
                NAME = message.author.name,
                ID = message.author.id,
                MSG = message.content,
                DATE = datetime.datetime.now()))
                                                                                                    
        self.cursor.execute(LOGSMSG.format(
        ID = message.author.id,
        NAME = message.author.name,
        CHNL = message.channel.name,
        MSG = str(message.content).replace("'",'').replace('"',''),
        DATE = datetime.datetime.now()))
        self.connection.commit()
        ic()


        
def prepare(client):
    client.add_cog(EventCog(client))