#! python3
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import traceback as tb
import praw
import pandas as pd
import datetime as dt
import re
import discord.voice_client
from discord.voice_client import VoiceClient
import redis
import random
from Credentials import *
TOKEN = ''


#scrapes redditAPI
reddit = praw.Reddit(client_id=clientid, \
                        client_secret=clientsecret, \
                        user_agent='redditapp for discord', \
                        username=reddusername, \
                        password=reddpw)




bot = commands.Bot(command_prefix='.')

"""@bot.command(name = "reddit", pass_context = True)
async def redditcom(ctx, subreddit):

    subreddit = reddit.subreddit(subreddit)
    for submission in subreddit.hot(limit=3):
        await ctx.send("{0}".format(submission.title))
        await ctx.send("{0}".format(submission.url))
For Bosslist, open txt file where to save the persons in list"""


@bot.command(name = "join", pass_context = True)
async def join(ctx, channel):
    await ctx.send("joining channel " + channel)
    await VoiceClient.join_voice_channel(channel)
    print("Bot joined the voice channel " + channel)


@bot.command(pass_context=True)
async def leave(ctx):
    await ctx.send("no")
    disconnect()

@bot.command()
async def apua(ctx):
    await ctx.send("!register - Komento bosslistille pääsemiseen, USAGE: !register USERNAME#1234")
    await ctx.send("!mp - bot tells his opinion about some user USAGE: !mp username")
    await ctx.send("!News -  Display top 3 posts today in r/news")    
    await ctx.send("!joined - bot tells you how long has somebody been on this server USAGE: !joined username")
    await ctx.send("!memes - Display top 3 posts today in r/dankmemes") 

bosslist = open('bosslist.txt','r')
List = bosslist.read().split(",")
print(List)
@bot.command()  
async def register(ctx, Name):
    if Name == str(ctx.message.author):
        if (Name) in List:
            await ctx.send("You are in the bosslist already")
        else:
            with open('bosslist.txt','a') as n:
                n.write("," + Name)
                List.append(Name)
                await ctx.send("You have been added to the bosslist")
                
    else:
        await ctx.send("THATS NOT YOU")





@bot.command()
async def mp(ctx, *, member: discord.Member):

    with open('bosslist.txt','r') as f:
        cont = f.read()
    if str(member) in cont:
        await ctx.send("{0} on Boss".format(member))

    else:
        await ctx.send("{0} ei ole Boss".format(member))

@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))




@bot.command()
async def memes(ctx):
    subreddit = reddit.subreddit('dankmemes')
    for submission in subreddit.hot(limit=3):
        await ctx.send("{0}".format(submission.title))
        await ctx.send("{0}".format(submission.url))

        
@bot.command()
async def news(ctx):
    subreddit = reddit.subreddit('news')
    for submission in subreddit.hot(limit=3):
        await ctx.send("{0}".format(submission.title))
        await ctx.send("{0}".format(submission.url))

@bot.command()
async def dota(ctx):
    subreddit = reddit.subreddit('dota2')
    for submission in subreddit.hot(limit=3):
        await ctx.send("{0}".format(submission.title))
        await ctx.send("{0}".format(submission.url))

@bot.command()
async def redfunny(ctx):
    subreddit = reddit.subreddit('funny')
    for submission in subreddit.hot(limit=3):
        await ctx.send("{0}".format(submission.title))
        await ctx.send("{0}".format(submission.url))

@bot.command()
async def funny(ctx):
    subreddit = reddit.subreddit('gifs')
    for submission in subreddit.hot(limit=3):
        await ctx.send("{0}".format(submission.title))
        await ctx.send("{0}".format(submission.url))





@bot.group(pass_context=True)
async def meemi(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('https://i.imgur.com/fhDxIh2.jpg'.format(ctx))




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)


