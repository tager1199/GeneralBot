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
import time
import pickle
from discord.utils import get
import youtube_dl
dir_path = os.path.dirname(os.path.realpath(__file__))
import urllib.request
from bs4 import BeautifulSoup


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

f = open("TOKEN.txt", "r")
TOKEN = f.read();
JokeStart = ["Today, my son asked \"Can I have a book mark?\" and I burst into tears.","My wife is really mad at the fact that I have no sense of direction.","DAD: I was just listening to the radio on my way in to town, apparently an actress just killed herself. \nMOM: Oh my! Who!? \nDAD: Uh, I can't remember... I think her name was Reese something? \nMOM: WITHERSPOON!!!!!???????","How do you make holy water?","I bought some shoes from a drug dealer.","Did you know the first French fries weren't actually cooked in France?","The secret service isn't allowed to yell \"Get down!\" anymore when the president is about to be attacked.","I'm reading a book about anti-gravity.","What do you call someone with no body and no nose?","I ordered a chicken and an egg from Amazon.","What is the least spoken language in the world?","My daughter screeched, \"Daaaaaad, you haven't listened to one word I've said, have you!?\"","A slice of apple pie is $2.50 in Jamaica and $3.00 in the Bahamas.","Did you know that's a popular cemetery?","My friend keeps saying \"cheer up man it could be worse, you could be stuck underground in a hole full of water.\"","Justice is a dish best served cold","The fattest knight at King Arthur’s round table was Sir Cumference.","MOM: \"How do I look?\"","Why can't you hear a pterodactyl go to the bathroom?","3 unwritten rules of life...","Don't trust atoms.","I told my son I was named after Thomas Jefferson… He said, \"But dad, your name is Brian.\"","KID: \"Dad, make me a sandwich!\"","Why did the invisible man turn down the job offer?","SERVER: \"Sorry about your wait.\"","What has two butts and kills people?","What did the pirate say on his 80th birthday?","CASHIER: \"Would you like the milk in a bag, sir?\"","What's the best part about living in Switzerland?","When an ambulance zips past with its siren blaring:","What do you call a dog that can do magic?","Why couldn't the bike standup by itself?","What do you call a deer with no eyes?","What you you call a deer with no eyes or legs?","What do you call a deer with no eyes and legs that's been hit by a car?","What do you call a deer with no eyes and legs that's on fire?","What do you call a fish with no eyes?","What’s Forrest Gump’s password?"]
JokeEnd = ["11 years old and he still doesn't know my name is Brian.","So I packed up my stuff and right.","DAD: No, it was with a knife...","You boil the hell out of it.","I don't know what he laced them with, but I was tripping all day!","They were cooked in Greece.","Now they have to yell \"Donald, duck!\"","It's impossible to put down!","Nobody knows.","I’ll let you know","Sign language","What a strange way to start a conversation with me...","These are the pie rates of the Caribbean.","Yep, people are just dying to get in there!","I know he means well.","If it were served warm it would be justwater.","He acquired his size from too much pi.","DAD: \"With your eyes.\"","Because the pee is silent.","1. \n2. \n3.","They make up everything!","I said, \"I know, but I was named AFTER Thomas Jefferson.\"","DAD: \"Poof, you’re a sandwich!\"","He couldn't see himself doing it.","DAD: \"Are you saying I’m fat?\"","An assassin","AYE MATEY","DAD: \"No, just leave it in the carton!\"","I don't know, but the flag is a big plus.","\"They won’t sell much ice cream driving that fast.\"","A Labracadabrador.","It was two tired.","No idea!","Still no idea!","Still no bloody idea!","Still no flaming idea!","Fsh","1Forrest1"]
Levels = {1:0,2:5,3:15,4:40,5:85,6:125,7:250,8:500,9:1000,10:1750}
players = {}
client = discord.Client()
ydl_opts = {
    'outtmpl': 'test.mp3',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

@client.event
async def on_message(message):

    rand = random.randint(0,200)
    text = message.content.lower()
    msg = ""
    #tpyes -1 = unkown, 0 = playing, 1 = streaming, 2 = listening, 3 = watching
    #await client.change_presence(game=discord.Game(name="myself", type=-1))

    #if message author is bot
    if message.author.bot == client.user:
        #stop the bot replying to itself
        return

    if message.author.bot == True:
        return

    #point_dic = load_obj("points")
    #if message.author in point_dic:
    #    if message.attachments != []:
    #        point_dic[message.author] = point_dic[message.author] + 5
    #    else:
    #        point_dic[message.author] = point_dic[message.author] + 1

    #elif message.attachments != []:
    #    point_dic[message.author] = 5
    #else:
    #    point_dic[message.author] = 1

    #save_obj(point_dic, 'points')


    if text == "$level":
        level = 0
        done = False
        while (not done) and (level != 10):
            if point_dic[message.author] > Levels[level+1]:
                level += 1
            else:
                done = True
        msg = "You are level: " + str(level)
        await message.channel.send(msg)
        await message.channel.send(msg)

    if text.startswith("hello tom bot"):
        msg = "Hello {0.author.mention}".format(message)
        await message.channel.send(msg)

    if text == "$ping":
        t = await message.channel.send('Pong!')
        ms = (t.timestamp-message.timestamp).total_seconds() * 1000
        await ms.edit(t, new_content='Pong! Took: {}ms'.format(int(ms)))

    if text.startswith("im"):
        msg = "Hi "
        for i in range(3, len(text)):
            msg += text[i]
        msg += " I'm Tom Bot"
        await message.channel.send(msg)

    if text.startswith("i'm"):
        msg = "Hi "
        for i in range(4, len(text)):
            msg += text[i]
        msg += " I'm Tom Bot"
        await message.channel.send(msg)

    if text == "$joke":
        jokeNo = random.randint(0,len(JokeStart)-1)
        await message.channel.send(JokeStart[jokeNo])
        time.sleep(1)
        await message.channel.send(JokeEnd[jokeNo])


    if text.startswith("tom bot is") and (text.endswith("real?") or text.endswith("real")):
        for i in range(10, len(text)-5):
            msg += text[i]
        if rand < 100:
             msg += " is not real"
        else:
            msg += " is real"

        await message.channel.send(msg)

    if text == "$join":
        author = message.author
        channel = author.voice.channel
        vc = await channel.connect()
        print(vc)
        server = message.guild
        players[server.id] = vc


    if text == "$disconnect":
        server = message.guild
        voice_client = server.voice_client
        await voice_client.disconnect()

    if text.startswith("$play "):
        search=""
        server = message.guild
        vc = players.get(server.id)
        print(vc)
        for i in range(6, len(text)):
            search += text[i]
        voice_client = server.voice_client
        query = urllib.parse.quote(search)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        url = 'https://www.youtube.com' + soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href']
        print(soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]['href'])
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        #player = await voice_client.create_ytdl_player(url)
        #players[server.id] = player
        #player.start()
        vc.play(discord.FFmpegPCMAudio('test.mp3'), after=lambda e: os.remove("test.mp3"))
        #vc.is_playing()
        #vc.pause()
        #vc.resume()
        #vc.source = discord.PCMVolumeTransformer(vc.source)
        #vc.source.volume = 0.6
        #vc.stop()


@client.event
#log basic info when the bot starts running
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)