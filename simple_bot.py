# -*- coding: utf-8 -*-
import asyncio
import discord
bot = discord.Client()

@asyncio.coroutine
def assign_region(message):
    region = message.content.strip('!region')
    author = message.author
    yield from bot.send_message(message.channel, "Hello {1}, you are in {0}" .format(region, author))


@bot.event
@asyncio.coroutine
def on_message(message):
    #author = message.author
    if message.content.startswith('!region'):
        yield from assign_region(message)

@bot.event
@asyncio.coroutine
def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

bot.run('Token')
