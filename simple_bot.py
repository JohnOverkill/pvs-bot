# -*- coding: utf-8 -*-
import asyncio
import discord
client = discord.Client()


# @asyncio.coroutine
# def assign_region(message):
#    region = message.content.replace('!region', '')
#    client.send_message(message.channel, region)


@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('!test'):
#         yield from assign_region(message)
         yield from client.send_message(message.channel, "hello")

client.run('MTk5NDY2MzA2ODc2MDgwMTI4.CmBsyg.pcJmTTObQn-cbDZcgGWRdXTjUq8')
