from discord.ext import commands
import discord
import asyncio

# token da api
TOKEN = ''

# prefixo antes dos comandos
client = commands.Bot(command_prefix = '.')
client.remove_command('help')

# confirma que esta rodando o bot
@client.event
async def on_ready():
	print("Beep beep beep AUDIO BOT IS READY[...]")

# JOINA E SAI DO CANAL DE VOZ
@client.command(pass_context=True)
async def join(ctx):
	author = ctx.message.author
	channel = author.voice_channel
	print(channel)
	await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await voice_client.disconnect()

""" ACTUAL AUDIO MESSAGES """
@client.command(pass_context=True)
async def tts(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('speech.mp3')
	player.start()

client.run(TOKEN)
