import re
import asyncio
import discord
from discord.ext import commands
from urllib.parse import urlparse

from config import TOKEN, GUILD_ID, INPUT_CHANNEL_ID, OUTPUT_CHANNEL_ID, OPENAI_API_KEY
from utils import extract_text_from_url, generate_summary, classify

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == INPUT_CHANNEL_ID:
        print("Message received in the input channel.")
        url_candidates = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
        urls = [url for url in url_candidates if urlparse(url).path]
        if urls:
            print(f"URL detected: {urls[0]}")
            loop = asyncio.get_event_loop()
            text = await loop.run_in_executor(None, extract_text_from_url, urls[0])
            print(text)
            print("Text extracted from URL.")
            summary = await generate_summary(text)
            print("Summary generated.")

            classify_result = await classify(text)
            print(classify_result)
            
            

            embed = discord.Embed(title="Summary", description=summary, color=0x5CDBF0)
            author_avatar_url = message.author.avatar.url if message.author.avatar else None
            embed.set_author(name=message.author.display_name, icon_url=author_avatar_url)

            output_channel = bot.get_channel(OUTPUT_CHANNEL_ID)
            if output_channel is None:
                print("Output channel not found. Creating a new output channel.")
                overwrites = {
                    message.guild.default_role: discord.PermissionOverwrite(read_messages=False)
                }
                output_channel = await message.guild.create_text_channel('output', overwrites=overwrites)

            print("Sending summary to output channel.")
            await output_channel.send(embed=embed)
            print("Summary sent.")
        else:
            print("No URL detected in the message.")

    await bot.process_commands(message)

bot.run(TOKEN)
