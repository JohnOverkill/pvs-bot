# -*- coding: utf-8 -*-
import asyncio
import discord
client = discord.Client()


#def assign_region(message):
#    region = message.content.strip('!region')
#    client.send_message(message.channel, region)


@client.event
@asyncio.coroutine
def on_message(message):
#    author = message.author
    if message.content.startswith('!region'):
         yield from client.send_message(message.channel, "Hi there")

client.run('MTk5NDY2MzA2ODc2MDgwMTI4.CmBsyg.pcJmTTObQn-cbDZcgGWRdXTjUq8')
