from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG
from msgs import *
import psutil
import platform

if not DEBUG:
    ic.disable() 
    
class MyCog(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ['инфо'])
    async def info(self, ctx):
        if ctx.author.name.lower() == "via___0":
            uname = platform.uname()
            cpufreq = psutil.cpu_freq()
            svmem = psutil.virtual_memory()
            a = ''
            a += f'System: {str(uname.system)} | Node Name: {uname.node} | Release: {uname.release[:9]} | Version: {uname.version} | Machine: {uname.machine} | Processor: {uname.processor}'
            a += f' | Physical cores: {psutil.cpu_count(logical=False)} | Total cores: {psutil.cpu_count(logical=True)} | '
            a += f'Max Frequency: {cpufreq.max:.2f}Mhz | Min Frequency: {cpufreq.min:.2f}Mhz | Current Frequency: {cpufreq.current:.2f}Mhz | '
            for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                a = a + f" Core {i + 1}: {percentage}% |"
                if (i + 1) % 4 == 0:
                    a = a + '\n'
            a += f'Total CPU Usage: {psutil.cpu_percent()}% | '
            a += f'Total MEM: {(await self.get_size(svmem.total))} | Available MEM: {(await self.get_size(svmem.available))} | Used MEM: {(await self.get_size(svmem.used))} | Percentage: {svmem.percent}%'
            await ctx.send(a)
            ic('INFS')
        else: 
            await ctx.send('ACCESS DENIED.')
            ic("ACCESS_DENY")
        ic()
        
def prepare(client):
    client.add_cog(MyCog(client))