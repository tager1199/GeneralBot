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
import asyncio
import random
import os
import time
import pickle
from discord.utils import get
import youtube_dl
dir_path = os.path.dirname(os.path.realpath(__file__))
import urllib.request
from bs4 import BeautifulSoup
from os.path import getmtime
import sys

playing = False
f = open("TOKEN.txt", "r")
TOKEN = f.read();
JokeStart = ["Today, my son asked \"Can I have a book mark?\" and I burst into tears.","My wife is really mad at the fact that I have no sense of direction.","DAD: I was just listening to the radio on my way in to town, apparently an actress just killed herself. \nMOM: Oh my! Who!? \nDAD: Uh, I can't remember... I think her name was Reese something? \nMOM: WITHERSPOON!!!!!???????","How do you make holy water?","I bought some shoes from a drug dealer.","Did you know the first French fries weren't actually cooked in France?","The secret service isn't allowed to yell \"Get down!\" anymore when the president is about to be attacked.","I'm reading a book about anti-gravity.","What do you call someone with no body and no nose?","I ordered a chicken and an egg from Amazon.","What is the least spoken language in the world?","My daughter screeched, \"Daaaaaad, you haven't listened to one word I've said, have you!?\"","A slice of apple pie is $2.50 in Jamaica and $3.00 in the Bahamas.","Did you know that's a popular cemetery?","My friend keeps saying \"cheer up man it could be worse, you could be stuck underground in a hole full of water.\"","Justice is a dish best served cold","The fattest knight at King Arthur’s round table was Sir Cumference.","MOM: \"How do I look?\"","Why can't you hear a pterodactyl go to the bathroom?","3 unwritten rules of life...","Don't trust atoms.","I told my son I was named after Thomas Jefferson… He said, \"But dad, your name is Brian.\"","KID: \"Dad, make me a sandwich!\"","Why did the invisible man turn down the job offer?","SERVER: \"Sorry about your wait.\"","What has two butts and kills people?","What did the pirate say on his 80th birthday?","CASHIER: \"Would you like the milk in a bag, sir?\"","What's the best part about living in Switzerland?","When an ambulance zips past with its siren blaring:","What do you call a dog that can do magic?","Why couldn't the bike standup by itself?","What do you call a deer with no eyes?","What you you call a deer with no eyes or legs?","What do you call a deer with no eyes and legs that's been hit by a car?","What do you call a deer with no eyes and legs that's on fire?","What do you call a fish with no eyes?","What’s Forrest Gump’s password?"]
JokeEnd = ["11 years old and he still doesn't know my name is Brian.","So I packed up my stuff and right.","DAD: No, it was with a knife...","You boil the hell out of it.","I don't know what he laced them with, but I was tripping all day!","They were cooked in Greece.","Now they have to yell \"Donald, duck!\"","It's impossible to put down!","Nobody knows.","I’ll let you know","Sign language","What a strange way to start a conversation with me...","These are the pie rates of the Caribbean.","Yep, people are just dying to get in there!","I know he means well.","If it were served warm it would be justwater.","He acquired his size from too much pi.","DAD: \"With your eyes.\"","Because the pee is silent.","1. \n2. \n3.","They make up everything!","I said, \"I know, but I was named AFTER Thomas Jefferson.\"","DAD: \"Poof, you’re a sandwich!\"","He couldn't see himself doing it.","DAD: \"Are you saying I’m fat?\"","An assassin","AYE MATEY","DAD: \"No, just leave it in the carton!\"","I don't know, but the flag is a big plus.","\"They won’t sell much ice cream driving that fast.\"","A Labracadabrador.","It was two tired.","No idea!","Still no idea!","Still no bloody idea!","Still no flaming idea!","Fsh","1Forrest1"]
Levels = {1:0,2:5,3:15,4:40,5:85,6:125,7:250,8:500,9:1000,10:1750}
players = {}
players_list = {}
Source = ""

client = discord.Client()
ydl_opts = {
    'outtmpl': 'song.mp3',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
def finish(player):
    os.remove('song.mp3')
    playing = False
    del players_list[player][0]
    play(player, "")


def play(player, request):
    if request != "":
        if player in players_list:
            players_list[player].append(request)
        else:
            players_list[player] = [request]


    url = players_list[player][0]
    if player.is_playing() == False and len(players_list[player]) > 0:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        Source = discord.FFmpegPCMAudio('song.mp3')
        player.play(Source, after=lambda e: finish(player))

def volume(player, number):
    if player.is_playing() == True:
        player.source = discord.PCMVolumeTransformer(Source)
        player.source.volume = number

def skip(player):
    if player.is_playing() == True:
        player.stop()
        play(player, "")

def pause(player):
    if player.is_playing() == True:
        player.pause()

def resume(player):
    try:
        player.resume()
    except:
        print("ERROR whilst pausing")

'''    if request != "":
        if player in players_list:
            players_list[player].append(request)
        else:
            players_list[player] = [request]
    url = players_list[player][0]
    print(player.is_playing())
    if player.is_playing() == False:
        if ((player not in players_list) or (len(players_list) == 1)):
            file = 'test.mp3'
            ydl_opts = {
                'outtmpl': file,
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            #player = await voice_client.create_ytdl_player(url)
            #players[server.id] = player
            #player.start()
        else:
            url = players_list[player][1]
            if not(os.path.isfile('test.mp3')):
                file = 'test.mp3'
                ydl_opts = {
                    'outtmpl': 'song.mp3',
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

            elif os.path.isfile('song.mp3'):
                file = 'song.mp3'
                ydl_opts = {
                    'outtmpl': 'test.mp3',
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

    else:
        if request != "":
            players_list[player].append(request)


    player.play(discord.FFmpegPCMAudio(file), after=lambda e: finish(player, file))




    #player.is_playing()
    #player.pause()
    #player.resume()
    #player.source = discord.PCMVolumeTransformer(vc.source)
    #player.source.volume = 0.6
    #player.stop()
'''

@client.event
async def on_message(message):

    rand = random.randint(0,200)
    text = message.content.lower()
    msg = ""
    author = message.author
    #tpyes -1 = unkown, 0 = playing, 1 = streaming, 2 = listening, 3 = watching
    #await client.change_presence(game=discord.Game(name="myself", type=-1))

    #if message author is bot
    if author.bot == client.user:
        #stop the bot replying to itself
        return

    if author.bot == True:
        return

    '''point_dic = load_obj("points")
    if message.author in point_dic:
        if message.attachments != []:
            point_dic[message.author] = point_dic[message.author] + 5
        else:
            point_dic[message.author] = point_dic[message.author] + 1

    elif message.attachments != []:
        point_dic[message.author] = 5
    else:
        point_dic[message.author] = 1

    save_obj(point_dic, 'points')
    point_dic = load_obj("points")
    '''

    if text == "$help":
        msg = "$level - Check your level. (Work in Progress)\n$ping - Check your ping\n$joke - Get the bot to tell a joke.\n$join - Get the bot to join the voice chat you're currently in.\n$disconnect - Disconnect the bot from whatever voice channel it is in.\
        \n$play [search] - Bot will search the search term on youtube and play the first result in the currently connected voice chat. \n$pause - pauses the music currently playing.\n$resume - Resumes paused music \n$skip - Skips the song currently playing\
        \nTom Bot is [something] real? - Tom Bot will tell you if something is real. \n ***!~Admin Only~!*** \n$restart - Restarts the bot to include any new features added recently \n\n***If you have an issue with the bot please contact tinyman1199#6969***"

        await message.channel.send(msg)

    if text == "$level":
        level = 0
        done = False
        while (not done) and (level != 10):
            if point_dic[author] > Levels[level+1]:
                level += 1
            else:
                done = True
        msg = "You are level: " + str(level)
        await message.channel.send(msg)

    if text.startswith("hello tom bot"):
        msg = "Hello {0.author.mention}".format(message)
        await message.channel.send(msg)

    if text == "$ping":
        t = await message.channel.send('Pong!')
        ms = (t.created_at-message.created_at).total_seconds() * 1000
        new_content = str('Pong! Took: {}ms'.format(int(ms)))
        await t.edit(content = new_content)

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
        channel = author.voice.channel
        vc = await channel.connect()
        server = message.guild
        players[server.id] = vc


    if text == "$disconnect":
        server = message.guild
        voice_client = server.voice_client
        players[server.id] = ""
        await voice_client.disconnect()

    if text.startswith("$play ") or text.startswith("$p "):
        pic = "https://img.youtube.com/vi/"
        await message.channel.send("Searching...")
        search=""
        server = message.guild
        vc = players.get(server.id)
        for i in range(6, len(text)):
            search += message.content[i]
        voice_client = server.voice_client
        query = urllib.parse.quote(search)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
        url = 'https://www.youtube.com' + info['href']
        id = ""
        for i in range(9, len(info['href'])):
            id += info['href'][i]

        for s in info:
            print(s)
        linkStart = ["https://www.youtube.com/watch","https://youtu.be/", "http://www.youtube.com/watch","http://youtu.be/", "www.youtube.com/watch", "youtu.be/", "youtube.com/watch"]
        for i in range(0,7):
            if search.startswith(linkStart[i]):
                url = search
                id = into['href'][-11:]

        pic += id + "/maxresdefault.jpg"
        e = discord.Embed(title = ("Found " + info['title']), description = "By - ")
        e.set_thumbnail(url=pic)
        await message.channel.send(embed = e)#+ " by " )
        if (vc in players_list) :
            if (url in players_list[vc]):
                await message.channel.send(info['title'] + " is already in the queue")
            else:
                play(vc,url)
        else:
            play(vc,url)

    if text.startswith("$volume "):
        search=""
        server = message.guild
        vc = players.get(server.id)
        for i in range(8, len(text)):
            search += text[i]
        num = float(search)
        if 1 <= num <= 100:
            volume(vc,num)
            await message.channel.send("Volume set to " + str(num))
        else:
            await message.channel.send("Volume must be between 1.0 and 100")

    if text == "$pause":
        server = message.guild
        vc = players.get(server.id)
        pause(vc)

    if text == "$resume":
        server = message.guild
        vc = players.get(server.id)
        resume(vc)

    if text == "$skip":
        server = message.guild
        vc = players.get(server.id)
        skip(vc)

    if text == "$restart":
        if ("admin" in [y.name.lower() for y in author.roles] or author.server_permissions.administrator == True):
            await message.channel.send("Restarting...")
            os.startfile(__file__)
            raise SystemExit


@client.event
#log basic info when the bot starts running
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
