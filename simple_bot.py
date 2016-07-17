# -*- coding: utf-8 -*-
import asyncio
import discord
bot = discord.Client()

@asyncio.coroutine
def add_euw(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='euw')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_euw(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='euw')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_eune(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='eune')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_eune(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='eune')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_na(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='na')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_na(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='na')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_oce(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='oce')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_oce(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='oce')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_las(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='las')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_las(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='las')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_lan(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='lan')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_lan(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='lan')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_br(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='br')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_br(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='br')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))

@bot.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('+!euw'):
        yield from add_euw(message)

    elif message.content.startswith('-!euw'):
        yield from remove_euw(message)

    elif message.content.startswith('+!eune'):
        yield from add_eune(message)

    elif message.content.startswith('-!eune'):
        yield from remove_eune(message)

    elif message.content.startswith('+!na'):
        yield from add_na(message)

    elif message.content.startswith('-!na'):
        yield from remove_na(message)

    if message.content.startswith('+!oce'):
        yield from add_oce(message)

    elif message.content.startswith('-!oce'):
        yield from remove_oce(message)

    elif message.content.startswith('+!las'):
        yield from add_las(message)

    elif message.content.startswith('-!las'):
        yield from remove_las(message)

    elif message.content.startswith('+!lan'):
        yield from add_lan(message)

    elif message.content.startswith('-!lan'):
        yield from remove_lan(message)

    elif message.content.startswith('+!br'):
        yield from add_br(message)

    elif message.content.startswith('-!br'):
        yield from remove_br(message)



@bot.event
@asyncio.coroutine
def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

bot.run('MTk5NDY2MzA2ODc2MDgwMTI4.CmBsyg.pcJmTTObQn-cbDZcgGWRdXTjUq8')
