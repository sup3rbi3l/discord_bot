# bot.py
from pytube import YouTube
import os
from discord import FFmpegPCMAudio
from discord.utils import get
from dotenv import load_dotenv
import asyncio
from discord import FFmpegPCMAudio
import discord
import asyncio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
print(TOKEN)
client = discord.Client(intents=discord.Intents.all())








@client.event
async def on_message(ctx):
    
    if ctx.author == client.user:
        return
    
    
    if ctx.content == '!blitz':
        channel = ctx.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            
        source = FFmpegPCMAudio('1.mp3')
        voice.play(source)
        await asyncio.sleep(5)
        await voice.disconnect()
        
        
        
    if ctx.content == '!sair':
        
        voice = get(client.voice_clients, guild=ctx.guild)
        await voice.disconnect()
    
    
    if ctx.content[0:2] == '!p':
        channel = ctx.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        link = ctx.content[3:]
        yt = YouTube(link)

        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = f'{base}.mp3'
        os.rename(out_file, new_file)
        
        source = FFmpegPCMAudio(new_file)
        voice.play(source)
        
        await asyncio.sleep(yt.length+1)
        print('funciona')
        os.remove(new_file)

        

client.run(TOKEN)