import os
import asyncio
from more_itertools import sliced
import discord
from discord import app_commands
from discord.ext import tasks, commands
from io import BytesIO
import requests
import re
from datetime import datetime, timedelta
from textwrap import wrap
from dotenv import load_dotenv
import threading
import gf2_embeds

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.all()
intents.members = True

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        intents.reactions = True
        self.synced = False

    async def on_ready(self):
        await client.change_presence(activity=discord.Game('with dolls'))
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=GUILD))
            self.synced = True
        self.loop.create_task(schedule_next_reminder())
        print(f"{self.user} is ready!")

client = aclient()
guild = discord.Object(id=GUILD)
tree = app_commands.CommandTree(client)


@tree.command(name = "iopwiki", description="Shows IOP Wiki information about the specified doll", guild=discord.Object(id=GUILD))
@app_commands.describe(doll="The doll you want to see information of")
async def embed_create(interaction: discord.Interaction, doll):
    doll = doll.lower()
    if doll == "wawa" or doll == "wa2000" or doll == "maki" or doll == "makiatto":
        await interaction.channel.send(embed=gf2_embeds.get_makiatto())
    else:
        await interaction.response.send_message("Something went wrong. Please contact Suzu.", ephemeral=True)
        
# @tree.command(name = "embededit", guild=discord.Object(id=GUILD))
# async def embed_create(interaction: discord.Interaction):
#     if interaction.user.id == 224589196235505665:
#         embed = discord.Embed(title="**Placeholder Embed**")
#         embed.add_field(name="placeholder 📷", value="placeholder value.", inline=False)
#         embed.set_thumbnail(url = "https://agilevelocity.com/wp-content/uploads/2018/03/work-98936_1280-300x300-1.png")
#         await interaction.channel.send(embed=embed)
#     else:
#         await interaction.response.send_message("You are not allowed to do that.", ephemeral=True)

def get_reset_time():
    now = datetime.utcnow()
    target = now.replace(hour=5, minute=0, second=0, microsecond=0)
    if now.hour > 5:
        target += timedelta(days=1)
    time_left = target - now 
    return f"{time_left.seconds // 3600}h {time_left.seconds % 3600 // 60}m"

@tree.command(name = "dailyreset", guild=discord.Object(id=GUILD))
async def embed_create(interaction: discord.Interaction):
    await interaction.response.send_message(f"There are {get_reset_time()} left until the next Global server reset.", ephemeral=True)

TARGET_TIMES = [
    (5, 0),
    (11, 0),
    (17, 0),
    (23, 0)
]

async def schedule_next_reminder():
    while True:
        now = datetime.utcnow()
        next_run = None
        for hour, minute in TARGET_TIMES:
            candidate = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if candidate > now:
                next_run = candidate
                break
        
        # If all times passed for today, schedule tomorrow's first time
        if not next_run:
            next_run = now + timedelta(days=1)
            next_run = next_run.replace(
                hour=TARGET_TIMES[0][0],
                minute=TARGET_TIMES[0][1],
                second=0,
                microsecond=0
            )

        wait_seconds = (next_run - now).total_seconds()
        print(f"Next reminder scheduled at {next_run} (in {wait_seconds} seconds).")
        
        # Sleep until the next reminder time
        await asyncio.sleep(wait_seconds)
        
        # Send the reminder
        await task()

async def task():
    print("Sending message...")
    await supply_reminder()

async def supply_reminder():
    channel = client.get_channel(1321452634284232777)  # Replace with valid channel ID
    try:
        sticker = await client.fetch_sticker(1323038318363152446)  # Replace with valid sticker ID
    except:
        sticker = None

    embed = discord.Embed(
        title="Friendly Reminder!",
        description=f"<@&{1323023802409554050}> Remember to pick up your free supplies from the shop!",
        color=0x3498db
    )
    if sticker:
        embed.set_image(url=sticker.url)

    await channel.send(embed=embed)

@tree.context_menu(name='Report Message', guild=guild)
async def report_message(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(
        f'This message by {message.author.mention} has been reported to the mods.', ephemeral=True
    )

    log_channel = interaction.guild.get_channel(1321475779279851550)

    embed = discord.Embed(title='Reported Message')
    if message.content:
        embed.description = message.content
    try:
        embed.set_thumbnail(url = message.attachments[0].url)
    except:
        print("")
    embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    embed.timestamp = message.created_at
    url_view = discord.ui.View()
    url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

    await log_channel.send(embed=embed, view=url_view) 



client.run(TOKEN)


