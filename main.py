import os
import discord
from discord.ext import commands
from openai import OpenAI

# Récupération des clés depuis les variables d'environnement
TOKEN_DISCORD = os.environ.get('DISCORD_TOKEN')
CLE_OPENAI = os.environ.get('OPENAI_API_KEY')

client_ai = OpenAI(api_key=CLE_OPENAI)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ JM AI est en ligne !")

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    if bot.user.mentioned_in(message):
        response = client_ai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es JM AI, créé par Jason de JMstudio."},
                {"role": "user", "content": message.content}
            ]
        )
        await message.reply(response.choices[0].message.content)

bot.run(TOKEN_DISCORD)
