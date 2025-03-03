import os
import asyncio
from more_itertools import sliced
import discord
from discord import app_commands
from discord.ui import Button
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
TARGET_TIMES = [
    (5, 0),
    (11, 0),
    (17, 0),
    (23, 0)
]

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
        await self.loop.create_task(schedule_reminders())
        print(f"{self.user} is ready!")

client = aclient()
guild = discord.Object(id=GUILD)
tree = app_commands.CommandTree(client)

class DollView(discord.ui.View):
    def __init__(self, base_embed: discord.Embed, images: list[str]):
        super().__init__()
        self.index = 0
        self.base_embed = base_embed
        self.images = images
        
    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬅️")
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.index = (self.index - 1) % len(self.images)
        embed = self._build_embed()
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="➡️")
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.index = (self.index + 1) % len(self.images)
        embed = self._build_embed()
        await interaction.response.edit_message(embed=embed, view=self)

    def _build_embed(self) -> discord.Embed:
        # Create a copy so you don't overwrite the original
        embed = self.base_embed.copy()
        embed.set_image(url=self.images[self.index])
        return embed


DOLL_IMAGES = {
    "makiatto": [
        "https://iopwiki.com/images/3/33/Macqiato_Whole.png",
        "https://iopwiki.com/images/thumb/9/98/Macqiato_costume1.png/1280px-Macqiato_costume1.png",
        "https://iopwiki.com/images/thumb/a/a8/Macqiato_3D.png/1280px-Macqiato_3D.png"
    ],
    "klukai": [
        "https://iopwiki.com/images/thumb/e/e4/Klukai_Whole.png/1280px-Klukai_Whole.png",
        "https://iopwiki.com/images/thumb/c/c9/Klukai_costume1.png/1280px-Klukai_costume1.png",
        "https://iopwiki.com/images/thumb/d/d0/Klukai_costume2.png/1280px-Klukai_costume2.png",
        "https://iopwiki.com/images/0/0d/Klukai_3D.png"
    ],
    "andoris": [
        "https://iopwiki.com/images/thumb/4/47/Andoris_Whole.png/1280px-Andoris_Whole.png",
        "https://iopwiki.com/images/2/29/Andoris_3D.png"
    ],
    "qiongjiu": [
        "https://iopwiki.com/images/thumb/e/ee/Qiongjiu_Whole.png/800px-Qiongjiu_Whole.png",
        "https://iopwiki.com/images/d/d2/Qiongju_3D.png"
    ],
    "mosin": [
        "https://iopwiki.com/images/thumb/3/39/Mosinnagant_Whole.png/1280px-Mosinnagant_Whole.png",
        "https://iopwiki.com/images/thumb/6/6a/Mosin-Nagant_%28GFL2%29_3D.png/1280px-Mosin-Nagant_%28GFL2%29_3D.png"
    ],
    "nagant": [
        "https://iopwiki.com/images/thumb/6/61/Nagant_Whole.png/800px-Nagant_Whole.png",
        "https://iopwiki.com/images/thumb/c/c1/Nagant_costume1.png/1280px-Nagant_costume1.png",
        "https://iopwiki.com/images/1/1d/Nagant_3D.png"
    ],
    "sharkry": [
        "https://iopwiki.com/images/thumb/a/ac/Sharkry_Whole.png/800px-Sharkry_Whole.png",
        "https://iopwiki.com/images/8/86/Sharky_3D.png"
    ],
    "cheeta": [
        "https://iopwiki.com/images/3/31/Cheeta_Whole.png",
        "https://iopwiki.com/images/thumb/8/8e/GFL2_Cheeta_costume1.png/1280px-GFL2_Cheeta_costume1.png",
        "https://iopwiki.com/images/c/c4/Cheeta_3D.png"
    ],
    "colphne": [
        "https://iopwiki.com/images/5/51/Colphne_Whole.png",
        "https://iopwiki.com/images/thumb/e/ef/Colphne_costume1.png/1280px-Colphne_costume1.png",
        "https://iopwiki.com/images/0/0c/Colphne_3D.png"
    ],
    "groza": [
        "https://iopwiki.com/images/thumb/2/24/Groza_Whole.png/1024px-Groza_Whole.png",
        "https://iopwiki.com/images/thumb/3/3f/Groza_costume3.png/1280px-Groza_costume3.png",
        "https://iopwiki.com/images/thumb/e/ec/Groza_costume1.png/1280px-Groza_costume1.png",
        "https://iopwiki.com/images/thumb/b/bb/Groza_costume2.png/1280px-Groza_costume2.png",
        "https://iopwiki.com/images/3/3a/Groza_3D.png"
    ],
    "krolik": [
        "https://iopwiki.com/images/thumb/d/d8/Charolic_Whole.png/1280px-Charolic_Whole.png",
        "https://iopwiki.com/images/thumb/d/d4/Krolik_costume2.png/1280px-Krolik_costume2.png",
        "https://iopwiki.com/images/thumb/1/1a/Charolic_costume1.png/1280px-Charolic_costume1.png",
        "https://iopwiki.com/images/8/82/Charolic_3D.png"
    ],
    "ksenia": [
        "https://iopwiki.com/images/thumb/f/f4/Ksenia_Whole.png/800px-Ksenia_Whole.png",
        "https://iopwiki.com/images/f/f9/Ksenia_%28GFL2%29_3D.png"
    ],
    "littara": [
        "https://iopwiki.com/images/thumb/f/f0/Littara_Whole.png/1280px-Littara_Whole.png",
        "https://iopwiki.com/images/3/3d/Littara_3D.png"
    ],
    "vepley": [
        "https://iopwiki.com/images/thumb/9/9d/Vepley_Whole.png/800px-Vepley_Whole.png",
        "https://iopwiki.com/images/thumb/f/ff/Vepley_costume1.png/1280px-Vepley_costume1.png",
        "https://iopwiki.com/images/thumb/6/6b/Vepley_costume2.png/1280px-Vepley_costume2.png",
        "https://iopwiki.com/images/2/26/Vepley_3D.png"
    ],
    "lotta": [
        "https://iopwiki.com/images/thumb/f/fb/Lotta_Whole.png/800px-Lotta_Whole.png",
        "https://gf2.mcc.wiki/image/doll/Avatar_Whole_LottaSR01.png",
        "https://iopwiki.com/images/1/18/Lotta_3D.png"
    ],
    "nemesis": [
        "https://iopwiki.com/images/thumb/a/aa/Nemesis_Whole.png/1280px-Nemesis_Whole.png",
        "https://iopwiki.com/images/thumb/3/34/Nemesis_costume2.png/1280px-Nemesis_costume2.png",
        "https://iopwiki.com/images/thumb/2/2c/Nemesis_costume3.png/1280px-Nemesis_costume3.png",
        "https://iopwiki.com/images/thumb/0/03/Nemesis_costume1.png/1280px-Nemesis_costume1.png",
        "https://iopwiki.com/images/2/2a/Nemesis_3D.png"
    ],
    "sabrina": [
        "https://iopwiki.com/images/thumb/9/94/Sabrina_Whole.png/1024px-Sabrina_Whole.png",
        "https://iopwiki.com/images/thumb/c/cb/Sabrina_costume1.png/1280px-Sabrina_costume1.png",
        "https://iopwiki.com/images/e/ed/Sabrina_3D.png"
    ],
    "suomi": [
        "https://iopwiki.com/images/thumb/8/87/Suomi_%28GFL2%29_Whole.png/800px-Suomi_%28GFL2%29_Whole.png",
        "https://iopwiki.com/images/thumb/1/1c/Suomi_%28GFL2%29_costume1.png/1280px-Suomi_%28GFL2%29_costume1.png",
        "https://iopwiki.com/images/a/ad/Suomi_%28GFL2%29_3D.png"
    ],
    "tololo": [
        "https://iopwiki.com/images/thumb/f/fc/Tololo_Whole.png/1024px-Tololo_Whole.png",
        "https://iopwiki.com/images/thumb/4/4f/Tololo_costume1.png/1280px-Tololo_costume1.png",
        "https://iopwiki.com/images/a/a7/Tololo_3D.png"
    ],
    "papasha": [
        "https://iopwiki.com/images/thumb/f/fe/Papasha_Whole.png/1280px-Papasha_Whole.png",
        "https://iopwiki.com/images/5/52/Papasha_3D.png"
    ],
    "peritya": [
        "https://iopwiki.com/images/thumb/a/af/Peritya_Whole.png/1024px-Peritya_Whole.png",
        "https://iopwiki.com/images/thumb/5/59/Peritya_costume1.png/1280px-Peritya_costume1.png",
        "https://iopwiki.com/images/7/7a/Peritya_3D.png"
    ],
    "ullrid": [
        "https://iopwiki.com/images/thumb/a/af/Ullrid_Whole.png/1280px-Ullrid_Whole.png",
        "https://iopwiki.com/images/0/03/Ullrid_3D.png"
    ],
    "vector": [
        "https://iopwiki.com/images/c/c0/Vector_Whole.png",
        "https://iopwiki.com/images/e/e7/Vector_%28GFL2%29_3D.png"
    ],
    "springfield": [
        "https://iopwiki.com/images/8/81/Springfield_%28GFL2%29_whole.png",
        "https://gf2.mcc.wiki/image/doll/Avatar_Whole_SpringfieldSSR01.png",
        "https://iopwiki.com/images/5/54/Springfield_%28GFL2%29_3D.png"
    ],
    "mechty": [
        "https://iopwiki.com/images/thumb/a/a4/Mechty_Whole.png/1280px-Mechty_Whole.png",
        "https://iopwiki.com/images/2/2c/Mechty_3D.png"
    ],
    "lenna": [
        "https://iopwiki.com/images/thumb/8/8f/Lenna_Whole.png/800px-Lenna_Whole.png",
        "https://gf2.mcc.wiki/image/doll/Avatar_Whole_LennaSSR01.png",
        "https://gf2.mcc.wiki/image/doll/Avatar_Whole_LennaSSR05.png",
        "https://iopwiki.com/images/d/d6/Lenna_3D.png"
    ],
    "centaureissi": [
        "https://iopwiki.com/images/thumb/3/32/Centaureissi_Whole.png/1280px-Centaureissi_Whole.png",
        "https://iopwiki.com/images/0/0d/Centaureissi_%28GFL2%29_3D.png"
    ],
    "dushevnaya": [
        "https://iopwiki.com/images/thumb/2/2a/Dushevnaya_Whole.png/1024px-Dushevnaya_Whole.png",
        "https://iopwiki.com/images/2/27/Dushevnaya_%28GFL2%29_3D.png"
    ],
    "daiyan": [
        "https://iopwiki.com/images/thumb/c/cc/Daiyan_Whole.png/1024px-Daiyan_Whole.png",
        "https://gf2.mcc.wiki/image/doll/Avatar_Whole_DaiyanSSR03.png",
        "https://iopwiki.com/images/b/b5/Daiyan_%28GFL2%29_3D.png"

    ],
    "zhaohui": [
        "https://iopwiki.com/images/thumb/7/7b/Zhaohui_Whole.png/1280px-Zhaohui_Whole.png",
        "https://iopwiki.com/images/thumb/e/e5/Zhaohui_costume1.png/1280px-Zhaohui_costume1.png",
        "https://iopwiki.com/images/3/31/Zhaohui_3D.png"
    ],
    "belka": [
        "https://iopwiki.com/images/thumb/8/8d/Belka_Whole.png/1280px-Belka_Whole.png",
        "https://gf2.mcc.wiki/image/doll/Avatar_Whole_BiyocaSSR01.png",
        "https://iopwiki.com/images/b/b0/Belka_3D.png"
    ],
    "faye": [
        "https://iopwiki.com/images/e/e1/Faye_whole.png",
        "https://iopwiki.com/images/4/4a/Faye_3D.png"
    ],
    "jiangyu": [
        "https://iopwiki.com/images/thumb/c/c8/Jiangyu_Whole.png/1280px-Jiangyu_Whole.png",
        "https://iopwiki.com/images/thumb/4/48/Jiangyu_%28GFL2%29_3D.png/1280px-Jiangyu_%28GFL2%29_3D.png"
    ],
    "peri": [
        "https://i.imgur.com/ZDbnaa8.png",
        "https://i.imgur.com/NBzz2n4.png"
    ]


}

DOLL_NAMES = {
   "makiatto": ["makiatto", "wa2000", "wawa", "wa2k", "maki"],
   "klukai": ["klukai", "clukay", "klukay", "416", "hk416"],
   "andoris": ["andoris"],
   "qiongjiu": ["qiongjiu", "qj"],
   "mosin": ["mosin", "mosin-nagant"],
   "nagant": ["nagant"],
   "sharkry": ["sharkry"],
   "cheeta": ["cheeta", "mp7"],
   "colphne": ["colphne"],
   "groza": ["groza", "ots", "ots-14", "ots14"],
   "krolik": ["krolik"],
   "ksenia": ["ksenia", "stechkin"],
   "littara": ["littara", "galil"],
   "vepley": ["vepr", "vepley", "vepr-12"],
   "lotta": ["lotta"],
   "nemesis": ["nemesis"],
   "sabrina": ["sabrina", "spas12", "spas-12", "spas"],
   "tololo": ["tll", "tololo"],
   "papasha": ["ppsh", "papasha"],
   "peritya": ["peritya", "cat", "catgirl"],
   "ullrid": ["ullrid"],
   "suomi": ["suo", "suomi"],
   "vector": ["vector"],
   "springfield": ["springfield"],
   "mechty": ["mechty", "g11"],
   "lenna": ["lenna", "ump9", "ump-9"],
   "centaureissi": ["centaureissi", "g36"],
   "dushevnaya": ["dush", "dushev", "dushevnaya", "ksvk"],
   "daiyan": ["type95", "daiyan", "type 95"],
   "zhaohui": ["zhaohui"],
   "jiangyu": ["jianyu", "type97", "type 97"],
   "faye": ["faye"],
   "peri": ["peri", "mp5"]

}

@tree.command(name = "iopwiki", description="Shows IOP Wiki information about the specified doll", guild=discord.Object(id=GUILD))
@app_commands.describe(doll="The doll you want to see information of")
async def embed_create(interaction: discord.Interaction, doll: str):
    normalized = doll.lower()
    base_embed, images = None, None
    
    for canonical_name, aliases in DOLL_NAMES.items():
        if normalized in aliases:
            base_embed = gf2_embeds.get_embed(canonical_name)
            images = DOLL_IMAGES[canonical_name]
            view = DollView(base_embed, images)
            # Set the embed image to the first one by default
            embed = base_embed.copy()
            embed.set_image(url=images[0])
            await interaction.response.send_message(embed=embed, view=view)

    if not base_embed:    
        await interaction.response.send_message("There's no doll with that name!", ephemeral=True)

async def get_reset_time():
    now = datetime.utcnow()
    target = now.replace(hour=5, minute=0, second=0, microsecond=0)
    if now.hour > 5:
        target += timedelta(days=1)
    time_left = target - now 
    return f"{time_left.seconds // 3600}h {time_left.seconds % 3600 // 60}m"

@tree.command(name = "dailyreset", description="Shows how many hours are left until daily reset", guild=discord.Object(id=GUILD))
async def embed_create(interaction: discord.Interaction):
    await interaction.response.send_message(f"There are {get_reset_time()} left until the next Global server reset.", ephemeral=True)

from datetime import datetime, timedelta
import asyncio
import discord

# Configuration
# Starting date: 01.03.2024 15:00 (assumed local time corresponds to 3pm Berlin time)
START_DATE = datetime(2025, 3, 1, 14, 0, 0)

CYCLE_LENGTH = 22       # Total days in cycle (8 active + 14 downtime)
ACTIVE_PHASE_DAYS = 8   # Days 0 to 7 (relative to cycle start) are active

async def schedule_reminders():
    while True:
        now = datetime.now()
        # Determine candidate time: today at 15:00 if in the future, otherwise tomorrow at 15:00
        today_3pm = now.replace(hour=14, minute=0, second=0, microsecond=0)
        candidate = today_3pm if now < today_3pm else today_3pm + timedelta(days=1)
        
        # Calculate cycle day based on candidate's date (ignoring time)
        days_since_start = (candidate.date() - START_DATE.date()).days
        cycle_day = days_since_start % CYCLE_LENGTH
        
        if cycle_day < ACTIVE_PHASE_DAYS:
            next_run = candidate
        else:
            # If candidate falls in downtime, compute the next active date (cycle resets to 0)
            days_to_add = CYCLE_LENGTH - cycle_day
            next_active_date = candidate.date() + timedelta(days=days_to_add)
            next_run = datetime.combine(next_active_date, candidate.time()).replace(hour=14, minute=0, second=0, microsecond=0)
        
        wait_seconds = (next_run - now).total_seconds()
        
        # Determine the message based on the cycle day of next_run
        next_cycle_day = ((next_run.date() - START_DATE.date()).days) % CYCLE_LENGTH
        if next_cycle_day == 0:
            message = "Tomorrow marks the start of the new Gunsmoke season! ARE YOU AS EXCITED AS I AM?!"
        elif next_cycle_day == 7:
            message = "This Gunsmoke season is nearly over~ Time to show off one last time!"
        else:
            message = "It's Gunsmoke season! Don't forget to give those baddies a good whoopin'!"
        
        print(f"Next reminder scheduled at {next_run} (in {wait_seconds} seconds). Message: {message}")
        await asyncio.sleep(wait_seconds)
        await send_reminder(message)

async def send_reminder(message):
    channel = client.get_channel(1321452634284232777)  # Replace with a valid channel ID
    embed = discord.Embed(
        title="Friendly Reminder!",
        description=message,
        color=0x3498db
    )
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

@client.event
async def on_raw_reaction_add(payload):
#print(payload.emoji)
    if payload.emoji.name == "✉️":
        #print("Working?")
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        try:
            await payload.member.send(message.content)
        except:
            print("no text")
        for attachment in message.attachments:
            await payload.member.send(attachment.url)
        print(payload.emoji.name)

replacements = {
    'x.com': 'fixupx.com',
    'instagram.com': 'ddinstagram.com',
    'pixiv.net': 'phixiv.net',
    'twitter.com': 'vxtwitter.com',
    'reddit.com': 'rxddit.com'
}


# Precompile regex once (outside message loop)
escaped_domains = map(re.escape, replacements.keys())
pattern = re.compile(
    r'\bhttps://(www\.)?(' + '|'.join(escaped_domains) + r')\b',
    flags=re.IGNORECASE
)

def replace_domain(match):
    return f'https://{replacements[match.group(2)]}'

@client.event
async def on_message(payload):
    result = ""
    if pattern.search(payload.content):
        result = pattern.sub(replace_domain, payload.content)
        channel = client.get_channel(payload.channel)
        # member = client.get_user(payload.id)
        name = payload.author.nick
        avatar_url = payload.author.avatar
        webhook = await payload.channel.create_webhook(name=name)
        await webhook.send(str(result), username=name, avatar_url=avatar_url)

        webhooks = await payload.channel.webhooks()
        for webhook in webhooks:
            await webhook.delete()
        await payload.delete()
        

@tree.context_menu(name="Forward Message to DMs", guild=guild)
async def forward_message(interaction: discord.Interaction, message: discord.Message):
    count = 0
    try:
        await interaction.user.send(message.content)
    except:
        print("no text")
    for attachment in message.attachments:
        await interaction.user.send(message.attachments[count].url)
        count += 1
    if message.attachments or message.content:
        await interaction.response.send_message(f'Successfully forwarded {message.author.mention}\'s message to your DMs.', ephemeral=True)
    else:
        await interaction.response.send_message(f'Something went wrong.', ephemeral=True)

client.run(TOKEN)


