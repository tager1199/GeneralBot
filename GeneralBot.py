#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Thomas
#
# Created:     26/03/2019
# Copyright:   (c) Thomas 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import discord
from discord.ext import commands
import random
import os
from discord.utils import get
dir_path = os.path.dirname(os.path.realpath(__file__))



f = open("TOKEN.txt", "r")
TOKEN = f.read();

client = discord.Client()
@client.event
async def on_message(message):
    rand = random.randint(0,200)

    #if message author is bot
    if message.author == client.user:
        #stop the bot replying to itself
        return

    if message.content.startswith('hello tom bot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('$ping'):
        t = await client.send_message(message.channel,'Pong!')
        ms = (t.timestamp-message.timestamp).total_seconds() * 1000
        await client.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))


    if message.content.startswith('$join'):
        author = message.author
        channel = author.voice_channel
        await client.join_voice_channel(channel)

@client.event
#log basic info when the bot starts running
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)