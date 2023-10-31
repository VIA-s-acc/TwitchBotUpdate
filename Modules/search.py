from twitchio.ext import commands
import sqlite3
import os.path
from icecream import ic
DIRorigin = os.path.abspath(os.path.join(os.getcwd()))
DBpath = os.path.join(DIRorigin, "bot.db")
from config import DEBUG
from msgs import *
import datetime
import wikipediaapi
from googlesearch import search

if not DEBUG:
    ic.disable() 
    
class SearchCog(commands.Cog):
    
    def __init__(self,client):
        self.client = client
        self.connection = sqlite3.connect(DBpath)
        self.cursor = self.connection.cursor()

    @commands.command(aliases = ['поиск'])
    async def search(self, ctx, query):
        wiki_wiki = wikipediaapi.Wikipedia(
            language='ru',
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent = UAGNT

        )
        page_py = wiki_wiki.page(query)
        if page_py.exists():
                msg = f"{ctx.author.name}, поиск по запросу <{query}> | "+page_py.text[0:min(len(page_py.text), 1500)]
                send_msg = msg[:499-len('...' + f' | URL: {page_py.fullurl}')]
                await ctx.send(send_msg  + '...' + f' | URL: {page_py.fullurl}')
                return
        search_results = search(query=query,num=3,lang='ru',stop=3,pause=0.0)
        i = 1
        mess = f'В wikipedia не было найдено соотвествующей информации по запросу <{query}>.\nНиже даны ссылки ,которые могут помочь.\n'
        for url in search_results:
                mess += f' | URL {i} : {url}'
                i += 1
        send_mess = mess[:490-len(f'{ctx.author.name}')]
        await ctx.send(f"{ctx.author.name}, {send_mess}" )
        
def prepare(client):
    client.add_cog(SearchCog(client))