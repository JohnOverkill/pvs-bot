# -*- coding: utf-8 -*-
import asyncio
import discord
client = discord.Client()


@client.async_event
def on_message(message):
    if message.content.startswith('!region'):
        region = message.content.replace('!region', '')
        await client.send_message(message.channel, region)

client.run('MTk5NDY2MzA2ODc2MDgwMTI4.CmBsyg.pcJmTTObQn-cbDZcgGWRdXTjUq8')
