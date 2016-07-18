# -*- coding: utf-8 -*-
import asyncio
import discord
bot = discord.Client()

@asyncio.coroutine
# servers
def add_euw(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='EUW')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_euw(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='EUW')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_eune(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='EUNE')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_eune(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='EUNE')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_na(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='NA')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_na(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='NA')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_oce(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='OCE')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_oce(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='OCE')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_las(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='LAS')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_las(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='LAS')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_lan(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='LAN')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_lan(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='LAN')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_br(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='BR')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_br(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='BR')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))
# ranks
def add_dia(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Diamond +')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_dia(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Diamond +')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_plat(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Platinum')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_plat(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Platinum')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_gold(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Gold')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_gold(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Gold')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_silver(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Silvers')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_silver(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Silvers')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_bronze(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Bronze')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_bronze(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Bronze')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))

# positions
def add_top(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Top')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_top(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Top')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_jungle(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Jungle')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_jungle(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Jungle')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))


def add_mid(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Mid')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_mid(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Mid')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))

def add_adc(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='ADC')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_adc(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='ADC')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))

def add_supp(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Support')
    yield from bot.add_roles(author, role)
    yield from bot.send_message(message.channel, "You have been added to {}" .format(role))

def remove_supp(message):
    author = message.author
    role = discord.utils.get(message.server.roles, name='Support')
    yield from bot.remove_roles(author, role)
    yield from bot.send_message(message.channel, "You have been removed from {}" .format(role))
@bot.event
@asyncio.coroutine
def on_message(message):
# servers
    if message.content.startswith('?!help'):
        yield from bot.send_message(message.channel, "You can add / remove roles via +!role and -!role. Available roles are 'NA', 'EUW', 'EUNE', 'OCE', 'LAS', 'LAN', 'BR', 'dia', 'plat', 'gold', 'silver', 'bronze', 'top', 'jungle', 'mid', 'adc' and  'supp'.")
    elif message.content.startswith('+!EUW'):
        yield from add_euw(message)

    elif message.content.startswith('-!EUW'):
        yield from remove_euw(message)

    elif message.content.startswith('+!EUNE'):
        yield from add_eune(message)

    elif message.content.startswith('-!EUNE'):
        yield from remove_eune(message)

    elif message.content.startswith('+!NA'):
        yield from add_na(message)

    elif message.content.startswith('-!NA'):
        yield from remove_na(message)

    elif message.content.startswith('+!OCE'):
        yield from add_oce(message)

    elif message.content.startswith('-!OCE'):
        yield from remove_oce(message)

    elif message.content.startswith('+!LAS'):
        yield from add_las(message)

    elif message.content.startswith('-!LAS'):
        yield from remove_las(message)

    elif message.content.startswith('+!LAN'):
        yield from add_lan(message)

    elif message.content.startswith('-!LAN'):
        yield from remove_lan(message)

    elif message.content.startswith('+!BR'):
        yield from add_br(message)

    elif message.content.startswith('-!BR'):
        yield from remove_br(message)

# ranks
    elif message.content.startswith('+!dia'):
        yield from add_dia(message)

    elif message.content.startswith('-!dia'):
        yield from remove_dia(message)

    elif message.content.startswith('+!plat'):
        yield from add_plat(message)

    elif message.content.startswith('-!plat'):
        yield from remove_plat(message)

    elif message.content.startswith('+!gold'):
        yield from add_gold(message)

    elif message.content.startswith('-!gold'):
        yield from remove_gold(message)

    elif message.content.startswith('+!silver'):
        yield from add_silver(message)

    elif message.content.startswith('-!silver'):
        yield from remove_silver(message)

    elif message.content.startswith('+!bronze'):
        yield from add_bronze(message)

    elif message.content.startswith('-!bronze'):
        yield from remove_bronze(message)

# postitions
    elif message.content.startswith('+!top'):
        yield from add_top(message)

    elif message.content.startswith('-!top'):
        yield from remove_top(message)

    elif message.content.startswith('+!jungle'):
        yield from add_jungle(message)

    elif message.content.startswith('-!jungle'):
        yield from remove_jungle(message)

    elif message.content.startswith('+!mid'):
        yield from add_mid(message)

    elif message.content.startswith('-!mid'):
        yield from remove_mid(message)

    elif message.content.startswith('+!adc'):
        yield from add_adc(message)

    elif message.content.startswith('-!adc'):
        yield from remove_adc(message)

    elif message.content.startswith('+!supp'):
        yield from add_supp(message)

    elif message.content.startswith('-!supp'):
        yield from remove_supp(message)

@bot.event
@asyncio.coroutine
def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

bot.run('MjA0MjczMjQ3MzAxMjcxNTUy.Cm1DyQ.9DRCligpGTcPDVRvVbS_v37y_Wk')
