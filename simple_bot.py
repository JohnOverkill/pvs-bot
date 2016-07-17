# -*- coding: utf-8 -*-
import asyncio
import discord
bot = discord.Client()

@asyncio.coroutine
def assign_euw(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='euw')
    yield from bot.add_roles(author, role)


@bot.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('+!euw'):
        yield from assign_euw(message)

@bot.event
@asyncio.coroutine
def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

bot.run('MTk5NDY2MzA2ODc2MDgwMTI4.CmBsyg.pcJmTTObQn-cbDZcgGWRdXTjUq8')
