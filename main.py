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

def format_string(s):
    s = s['parameters']
    #print("parameters before:\n " + s)
    s = s.replace("\n","")
    #print("\n______________________________\nparameters after s:\n " + s)
    result = {}
    result['Positive prompt'] = s.split('Negative prompt: ')[0].strip()
    repara = result['Positive prompt']
    
    #print(repara)
    if "Negative prompt" in repara and repara[repara.index("Negative prompt")-1] != " ":
        index = repara.index("Negative prompt")
        result['Positive prompt'] = repara[:index] + " "

    if "Negative prompt:" in repara and repara[repara.index("Negative prompt:")+17] != " ":
        index = repara.index("Negative prompt:")
        result['Positive prompt'] = repara[:index+16] + " " 

    #print("result positive prompt:" + result['Positive prompt'])
    if "Steps" in s:
        index = s.index("Steps")
        s = s[:index] + ", " + s[index:]
        #print(f"\n\nS: \n{s}")
    for category in s.split(','):
        #print("category: "+ category)
        
        if 'Negative prompt' in result['Positive prompt']:
            result['Positive prompt'] = result['Positive prompt'].replace("Negative prompt", "") 
        elif 'Negative prompt: ' in category:
            np = "Negative prompt:"
            st = "Steps"
            idx1 = s.index(np)
            idx2 = s.index(st)
            result["Negative prompt"] = s[idx1 + len(np) + 1: idx2-2]
        elif 'Steps: ' in category:
            st = "Steps:"
            sa = ", Sampler"
            idx1 = s.index(st)
            idx2 = s.index(sa)
            result["Steps"] = s[idx1 + len(st) + 1: idx2]
        elif ': ' in category:
            key, value = category.split(': ', 1)
            result[key.strip()] = value.strip()
    return result


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        intents.reactions = True
        self.synced = False

    async def on_ready(self):
        await client.change_presence(activity=discord.Game('with small tiddeys'))
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=GUILD))
            self.synced = True

client = aclient()
guild = discord.Object(id=GUILD)
tree = app_commands.CommandTree(client)


@tree.command(name = "embedcreate", guild=discord.Object(id=GUILD))
async def embed_create(interaction: discord.Interaction):
    if interaction.user.id == 1015300244600258590:
        embed = discord.Embed(title="**Unlock Channels**")
        embed.add_field(name="realistic 📷", value="Realistic depictions of individuals or scenery.", inline=False)
        embed.add_field(name="girls 👧🏻", value="Female humanoids in their teens or pre-teens.", inline=False)
        embed.add_field(name="boys 👦🏻", value="Male humanoids in their teens or pre-teens", inline=False)
        embed.add_field(name="misc 🌆", value="Anything not fit for other channels.", inline=False)
        embed.add_field(name="non-humanoid 🐱", value="Centaurs, cthulhus, you name it.", inline=False)
        embed.add_field(name="non-con 💉", value="When you can't afford the prostitute.", inline=False)
        embed.add_field(name="national-geographic 🐈", value="Deep insights into the animal kingdom. No artstyle restrictions.", inline=False)
        embed.add_field(name="scatman ☕", value="You like your coffee as it comes.", inline=False)
        embed.add_field(name="unalived 🪦", value="Used but in good condition. No returns.", inline=False)
        embed.add_field(name="butcher's 🍖", value="Used. ~~Item defective. No returns~~", inline=False)
        embed.set_thumbnail(url = "https://agilevelocity.com/wp-content/uploads/2018/03/work-98936_1280-300x300-1.png")
        await interaction.channel.send(embed=embed)
    else:
        await interaction.response.send_message("Only unpaid interns are allowed to do that!", ephemeral=True)
        
@tree.command(name = "embededit", guild=discord.Object(id=GUILD))
async def embed_create(interaction: discord.Interaction):
    if interaction.user.id == 1015300244600258590:
        embed = discord.Embed(title="**Unlock Channels**")
        embed.add_field(name="realistic 📷", value="Realistic depictions of individuals or scenery.", inline=False)
        embed.add_field(name="girls 👧🏻", value="Female humanoids that appear not to be adults.", inline=False)
        embed.add_field(name="boys 👦🏻", value="Male humanoids that appear not to be adults.", inline=False)
        embed.add_field(name="misc 🌆", value="Anything not fit for other channels.", inline=False)
        embed.add_field(name="non-humanoid 🐱", value="Centaurs, cthulhus, you name it.", inline=False)
        embed.add_field(name="non-con 💉", value="When you can't afford the prostitute.", inline=False)
        embed.add_field(name="national-geographic 🐈", value="Deep insights into the animal kingdom. No artstyle restrictions.", inline=False)
        embed.add_field(name="scatman ☕", value="You like your coffee as it comes.", inline=False)
        embed.add_field(name="unalived 🪦", value="Used but in good condition. No returns.", inline=False)
        embed.add_field(name="butcher's 🍖", value="Used. ~~Item defective. No returns~~", inline=False)
        embed.set_thumbnail(url = "https://agilevelocity.com/wp-content/uploads/2018/03/work-98936_1280-300x300-1.png")
        await interaction.channel.send(embed=embed)
    else:
        await interaction.response.send_message("Only unpaid interns are allowed to do that!", ephemeral=True)

@tree.context_menu(name="Get Metadata", guild=discord.Object(id=GUILD))
async def get_metadata(interaction: discord.Interaction, message: discord.Message):
    metadata = extract_metadata(message)
    if metadata is None:
        await interaction.response.send_message("The message you have selected does not contain any attachments to extract metadata from.", ephemeral=True)
        return
    positive_prompts = []
    negative_prompts = []
    count = 0
    for data in metadata:
        try:
            data = format_string(data)
        except Exception as e:
            await interaction.response.send_message(f"Metadata for this media file does not exist.", ephemeral=True)
            return
        url = message.attachments[count].url
        count += 1
        #print(f"DATA: {data}")
        if not data['Positive prompt'] == "Steps" and not data['Positive prompt'] == "" and not data['Positive prompt'] == " ":
            positive_prompt = data['Positive prompt']
        else:
            positive_prompt = "`Empty`"
        #print(positive_prompt)
        if len(positive_prompt) +  len(data['Negative prompt']) > 5999:
            embed = discord.Embed()
            embed.add_field(name="Error",value="Discord doesn't support embeds with over 6000 characters.\nPlease use the WebUI or [other services](<https://www.metadata2go.com/>) to extract metadata for now.")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        if len(positive_prompt) > 1023:
            positive_prompts = list(sliced(positive_prompt, 1024))
        try:
            negative_prompt = data['Negative prompt']
        except:
            negative_prompt = "`Empty`"
        if len(negative_prompt) > 1023:
            negative_prompts = list(sliced(negative_prompt, 1024))
        
        #print("DATA: \n")
        #print(data)
        try:
            steps = data['Steps']
            if steps.endswith(", "):
                steps.split(", ")
        except:
            print("Steps still not working.")
        sampler = data['Sampler']
        cfg_scale = data['CFG scale']
        seed = data['Seed']
        size = data['Size']
        try:
            model_hash = data['Model hash']
        except:
            model_hash = "Unknown Hash"
            print("No model hash.")
        try:
            model = data['Model']
        except:
            if model_hash == '8712e20a5d':
                model = "AnythingV3"
            else:
                model = "Unknown"
        try:
            denoise_str = data['Denoising strength']
            hires_upscale = data['Hires upscale']
            hires_upscaler = data['Hires upscaler']
        except:
            print("")
        embed = discord.Embed(title='**Generation Parameters**')
        embed.set_thumbnail(url = url)
        embed.timestamp = message.created_at
        i = 0
        
        if positive_prompts:
            for prompt in positive_prompts:
                if i == 0:
                    embed.add_field(name="Positive Prompt", value=prompt, inline=False)
                    i += 1
                else:
                    embed.add_field(name="", value=prompt, inline=False)
        else:
            embed.add_field(name="Positive Prompt", value=positive_prompt, inline=False)
        j = 0
        if negative_prompts:
            for prompt in negative_prompts:
                if j == 0:
                    embed.add_field(name="Negative Prompt", value=prompt, inline=False)
                    j += 1
                else:
                    embed.add_field(name="", value=prompt, inline=False)
        else:
            embed.add_field(name="Negative Prompt", value=negative_prompt, inline=False)
        embed.add_field(name="Sampler", value=sampler)
        embed.add_field(name="Steps", value=steps)
        embed.add_field(name="CFG-Scale", value=cfg_scale)
        embed.add_field(name="Seed", value=seed)
        embed.add_field(name="Resolution", value=size)
        try:
            embed.add_field(name="Denoising Strength", value=denoise_str)
            embed.add_field(name="Hires Upscaler", value=f'{hires_upscaler}: x{hires_upscale}')
        except:
            embed.add_field(name="Hires Upscaler", value="`None`")
            print("No upscaler used.")
        embed.add_field(name="Model", value=f'{model} ({model_hash})', inline=False)
        embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)

        try:
            print(f"Embed requested: \n {embed}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            print(embed)
            await interaction.followup.send(embed=embed, ephemeral=True)

@tree.context_menu(name="Get Raw Metadata", guild=discord.Object(id=GUILD))
async def get_raw_metadata(interaction: discord.Interaction, message: discord.Message):
    
    metadata = extract_metadata(message)
    metadata = metadata[0]['parameters']
    #message = f'{metadata[17:3]}'
    embed = discord.Embed(title='**Generation Parameters**')
    embed.add_field(name="Raw", value=metadata, inline=False)
    if metadata is None:
        await interaction.response.send_message("The message you have selected does not contain any attachments to extract metadata from.", ephemeral=True)
        return
    else:
        await interaction.response.send_message(embed=embed, ephemeral=True)

@tree.context_menu(name="POST via API", guild=discord.Object(id=GUILD))
async def postAPI(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message("WIP. Make sure to have '--api' in your commandline args to enable the API and make use of this feature.", ephemeral=True)
    return
    

@tree.context_menu(name="Save Image to DMs", guild=guild)
async def forward_message(interaction: discord.Interaction, message: discord.Message):
    count = 0
    for attachment in message.attachments:
        await interaction.user.send(message.attachments[count].url)
        count += 1
    if message.attachments:
        await interaction.response.send_message(f'Successfully forwarded {message.author.mention}\'s image to your DMs.', ephemeral=True)
    else:
        await interaction.response.send_message(f'The message you selected does not contain any images.', ephemeral=True)

@client.event
async def on_raw_reaction_add(payload):
#print(payload.emoji)
    if payload.emoji.name == "✉️":
        #print("Working?")
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        for attachment in message.attachments:
            await payload.member.send(attachment.url)
    print(payload.emoji.name)
    
@tree.context_menu(name='Report Message', guild=guild)
async def report_message(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(
        f'This message by {message.author.mention} has been reported to the mods.', ephemeral=True
    )

    log_channel = interaction.guild.get_channel(1074655839866069062)

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
