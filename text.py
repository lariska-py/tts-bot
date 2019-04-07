from discord.ext import commands
from gtts import gTTS
import discord
import asyncio


TOKEN = ''

def tts(x, l):
	text_input = x
	language = l
	audio = gTTS(text=text_input, lang=language, slow=False) 
	audio.save("speech.mp3") 

# prefixo antes dos comandos
client = commands.Bot(command_prefix = '.')

# confirma que esta rodando o bot
@client.event
async def on_ready():
	print("Beep beep beep TTS IS READY [...]")

# get message to mp3 file
@client.event
async def on_message(message):
	if message.content.startswith("say"):
		txt = message.content[4:-3]
		if '-' in message.content:
			lang = message.content[-2:]
		else:
			lang = 'it'
		# await client.send_message(message.channel, message.content[4:])
		tts(txt, lang)

client.run(TOKEN)
