import os
from more_itertools import sliced
import discord
from discord import app_commands
from discord.ext import commands
from PIL import Image
from io import BytesIO
import requests
import re
from textwrap import wrap
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.all()
intents.members = True

def extract_metadata(message):
    if not message.attachments:
        return None
    content = message.attachments
    #print("content: "+ content[0].url +"\n" )
    count = 0
    urls = []
    metadata = []
    for attachment in content:
        #print("attachment: " + attachment.url)
        #print("\nfilename: " + attachment.filename)
        try:
            #print("inside try")
            if attachment.filename.endswith(".png") or attachment.filename.endswith(".jpg") or attachment.filename.endswith(".webp"):
                urls.append(attachment.url)
                count += 1
                print(count)
        except Exception as e:
            print(e)
    for url in urls:
        #print("url in urls: " + url)
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        data = img.info
        formatted = data
        metadata.append(formatted)
    return metadata

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

client = aclient()
guild = discord.Object(id=GUILD)
tree = app_commands.CommandTree(client)


@tree.command(name = "embedcreate", guild=discord.Object(id=GUILD))
async def embed_create(interaction: discord.Interaction):
    if interaction.user.id == 224589196235505665:
        embed = discord.Embed(title="**Placeholder Embed**")
        embed.add_field(name="placeholder 📷", value="placeholder value.", inline=False)
        embed.set_thumbnail(url = "https://agilevelocity.com/wp-content/uploads/2018/03/work-98936_1280-300x300-1.png")
        await interaction.channel.send(embed=embed)
    else:
        await interaction.response.send_message("You are not allowed to do that.", ephemeral=True)
        
@tree.command(name = "embededit", guild=discord.Object(id=GUILD))
async def embed_create(interaction: discord.Interaction):
    if interaction.user.id == 224589196235505665:
        embed = discord.Embed(title="**Placeholder Embed**")
        embed.add_field(name="placeholder 📷", value="placeholder value.", inline=False)
        embed.set_thumbnail(url = "https://agilevelocity.com/wp-content/uploads/2018/03/work-98936_1280-300x300-1.png")
        await interaction.channel.send(embed=embed)
    else:
        await interaction.response.send_message("You are not allowed to do that.", ephemeral=True)
    
@tree.context_menu(name='Report Message', guild=guild)
async def report_message(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(
        f'This message by {message.author.mention} has been reported to the mods.', ephemeral=True
    )

    log_channel = interaction.guild.get_channel(1321445392117796965)

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
