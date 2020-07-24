#Bot.py
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!")
client = discord.Client()
zz

@bot.command(pass_context=True)
async def leave(ctx):
    voiceChannel = await disconnect_channel(ctx)

@bot.command(pass_context=True)
async def join(ctx):
    voiceChannel = await load_voice_channel(ctx)

@bot.command(pass_context=True)
async def foguete(ctx):
    voiceChannel = await load_voice_channel(ctx)
    source = await load_sound_source('./sounds/foguete.mp3')
    voiceChannel.play(source)
    voiceChannel.is_playing()

@bot.command(pass_context=True)
async def brasil(ctx):
    voiceChannel = await load_voice_channel(ctx)
    source = await load_sound_source('./sounds/brasil.mp3')
    voiceChannel.play(source)
    voiceChannel.is_playing()
    
@bot.command(pass_context=True)
async def senna(ctx):
    voiceChannel = await load_voice_channel(ctx)
    source = await load_sound_source('./sounds/senna.mp3')
    voiceChannel.play(source)
    voiceChannel.is_playing()
    
@bot.command(pass_context=True)
async def missao(ctx):
    voiceChannel = await load_voice_channel(ctx)
    source = await load_sound_source('./sounds/missao.mp3')
    voiceChannel.play(source)
    voiceChannel.is_playing()

@bot.command(pass_context=True)
async def missaobugada(ctx):
    voiceChannel = await load_voice_channel(ctx)
    source = await load_sound_source('./sounds/missaobugada.mp3')
    voiceChannel.play(source)
    voiceChannel.is_playing()

@bot.command(pass_context=True)
async def gremio(ctx):
    voiceChannel = await load_voice_channel(ctx)
    source = await load_sound_source('./sounds/gremio.mp3')
    voiceChannel.play(source)
    voiceChannel.is_playing()


bot.run(TOKEN)