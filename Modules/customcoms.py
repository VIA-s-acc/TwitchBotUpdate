from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG
from msgs import *
import datetime
import sys
import time
if not DEBUG:
    ic.disable() 
    
class CustomComs(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ["ДобКом"])
    async def add_comm(self, ctx, comm_name, comm_text):
        if ctx.author.name.lower() == "via___0" or ctx.author.name.lower() == ctx.channel.name:
            for i in ",./*-+1234567890!@#$%`&()_:';~":
                if i in comm_name:
                    await ctx.send(CCSYMERR)
                    return
            if len(comm_name.split(' ')) > 1:
                await ctx.send(CNERR.format(comm_name=comm_name))
                return
            self.cursor.execute(COMMSET.format(
                CHNL = ctx.channel.name,
                COMM = comm_name,
                TXT = comm_text))
            self.connection.commit()
            await ctx.send("Success.")
            ic()
        else: 
            await ctx.send('ACCESS DENIED.')
            ic("ACCESS_DENY")
        
    @commands.command(aliases = ["УдлКом"])
    async def del_comm(self, ctx, comm_name):
        if ctx.author.name.lower() == "via___0" or ctx.author.name.lower() == ctx.channel.name:

            if self.cursor.execute(CCCHECK.format(
                COMM = comm_name,
                CHNL = ctx.channel.name)).fetchone() is not None:
                    self.cursor.execute(COMMDEL.format(
                    CHNL = ctx.channel.name,
                    COMM = comm_name))
            self.connection.commit()
            await ctx.send("Success.")
        else: 
            await ctx.send('ACCESS DENIED.')
            ic("ACCESS_DENY")
        ic()
            
   
    
        
def prepare(client):
    client.add_cog(CustomComs(client))