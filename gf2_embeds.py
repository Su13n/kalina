import discord

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
        "https://iopwiki.com/images/thumb/9/98/Macqiato_costume1.png/1280px-Macqiato_costume1.png"
    ],
    "klukai": [
        "https://example.com/klukai1.png",
        "https://example.com/klukai2.png"
    ],
    # ...
}

def get_makiatto():
    embed = discord.Embed(title="Makiatto",
                        url="https://iopwiki.com/wiki/Makiatto",
                        colour=0xf40068)

    embed.set_author(name="IOP Wiki",
                    url="https://iopwiki.com/",
                    icon_url="https://iopwiki.com/favicon.ico")

    embed.add_field(name="Rarity",
                    value="Elite",
                    inline=True)
    embed.add_field(name="Affiliation",
                    value="Zucchero Café",
                    inline=True)
    embed.add_field(name="Body type",
                    value="SSD-62D",
                    inline=False)
    embed.add_field(name="Role",
                    value="Sentinel",
                    inline=True)
    embed.add_field(name="Speciality",
                    value="Single Target Damage / First Strike",
                    inline=False)
    embed.add_field(name="Signature Weapon",
                    value="WA2000",
                    inline=True)
    embed.add_field(name="Weapon Type",
                    value="RF",
                    inline=True)
    embed.add_field(name="Imprint Boost",
                    value="[Bittersweet Caramel](https://iopwiki.com/wiki/GFL2_Weapons#RF)",
                    inline=False)
    embed.add_field(name="Affinities",
                    value="Heavy Ammo / Freeze",
                    inline=True)
    embed.add_field(name="Weaknesses",
                    value="Light Ammo / Burn",
                    inline=True)
    embed.add_field(name="Personality",
                    value="Courage",
                    inline=False)

    #embed.set_image(url="https://iopwiki.com/images/3/33/Macqiato_Whole.png")

    embed.set_thumbnail(url="https://iopwiki.com/images/a/a9/Makiatto_S.png")

    embed.set_footer(text="Azure",
                    icon_url="https://cdn.discordapp.com/icons/1321437165774700575/ca4f95365bd06f8e9809c359185acc0d.webp")

    return embed

def get_andoris():
    embed = discord.Embed(title="Andoris",
                      url="https://iopwiki.com/wiki/Andoris",
                      colour=0xf40068)

    embed.set_author(name="IOP Wiki",
                    url="https://iopwiki.com/",
                    icon_url="https://iopwiki.com/favicon.ico")

    embed.add_field(name="Rarity",
                    value="Elite",
                    inline=True)
    embed.add_field(name="Affiliation",
                    value="H.I.D.E 404",
                    inline=True)
    embed.add_field(name="Body type",
                    value="SSD-62F",
                    inline=False)
    embed.add_field(name="Role",
                    value="Bulwark",
                    inline=True)
    embed.add_field(name="Speciality",
                    value="?",
                    inline=False)
    embed.add_field(name="Signature Weapon",
                    value="G36-KSK",
                    inline=True)
    embed.add_field(name="Weapon Type",
                    value="AR",
                    inline=True)
    embed.add_field(name="Imprint Boost",
                    value="[Aglaea](https://iopwiki.com/wiki/GFL2_Weapons#AR)",
                    inline=False)
    embed.add_field(name="Affinities",
                    value="Medium Ammo / Electric",
                    inline=True)
    embed.add_field(name="Weaknesses",
                    value="Heavy Ammo / Corrosion",
                    inline=True)
    embed.add_field(name="Personality",
                    value="?",
                    inline=False)

    embed.set_image(url="https://iopwiki.com/images/thumb/4/47/Andoris_Whole.png/1280px-Andoris_Whole.png")

    embed.set_thumbnail(url="https://iopwiki.com/images/9/91/Andoris_S.png")

    embed.set_footer(text="Azure",
                    icon_url="https://cdn.discordapp.com/icons/1321437165774700575/ca4f95365bd06f8e9809c359185acc0d.webp")
    
    return embed

def get_klukai():
    embed = discord.Embed(title="Clukay",
                        url="https://iopwiki.com/wiki/Klukai",
                        colour=0xf40068)

    embed.set_author(name="IOP Wiki",
                    url="https://iopwiki.com/",
                    icon_url="https://iopwiki.com/favicon.ico")

    embed.add_field(name="Rarity",
                    value="Elite",
                    inline=True)
    embed.add_field(name="Affiliation",
                    value="H.I.D.E 404",
                    inline=True)
    embed.add_field(name="Body type",
                    value="SST-05",
                    inline=False)
    embed.add_field(name="Role",
                    value="Sentinel",
                    inline=True)
    embed.add_field(name="Speciality",
                    value="?",
                    inline=False)
    embed.add_field(name="Signature Weapon",
                    value="HK416",
                    inline=True)
    embed.add_field(name="Weapon Type",
                    value="AR",
                    inline=True)
    embed.add_field(name="Imprint Boost",
                    value="[Scylla](https://iopwiki.com/wiki/GFL2_Weapons#AR)",
                    inline=False)
    embed.add_field(name="Affinities",
                    value="Medium Ammo / Corrosion",
                    inline=True)
    embed.add_field(name="Weaknesses",
                    value="Shotgun Ammo / Electric",
                    inline=True)
    embed.add_field(name="Personality",
                    value="?",
                    inline=False)

    embed.set_image(url="https://iopwiki.com/images/thumb/e/e4/Klukai_Whole.png/1280px-Klukai_Whole.png")

    embed.set_thumbnail(url="https://iopwiki.com/images/thumb/1/11/Klukai_S.png/250px-Klukai_S.png")

    embed.set_footer(text="Azure",
                    icon_url="https://cdn.discordapp.com/icons/1321437165774700575/ca4f95365bd06f8e9809c359185acc0d.webp")

    return embed

def get_qiongjiu():
    embed = discord.Embed(title="Qiongjiu",
                      url="https://iopwiki.com/wiki/Qiongjiu",
                      colour=0xf40068)

    embed.set_author(name="IOP Wiki",
                    url="https://iopwiki.com/",
                    icon_url="https://iopwiki.com/favicon.ico")

    embed.add_field(name="Rarity",
                    value="Elite",
                    inline=True)
    embed.add_field(name="Affiliation",
                    value="G&K \"Frostfall\" Team",
                    inline=True)
    embed.add_field(name="Body type",
                    value="SSD-62G",
                    inline=False)
    embed.add_field(name="Role",
                    value="Sentinel",
                    inline=True)
    embed.add_field(name="Speciality",
                    value="Sustained Damage / Assist",
                    inline=False)
    embed.add_field(name="Signature Weapon",
                    value="QBZ-191",
                    inline=True)
    embed.add_field(name="Weapon Type",
                    value="AR",
                    inline=True)
    embed.add_field(name="Imprint Boost",
                    value="[Golden Melody](https://iopwiki.com/wiki/GFL2_Weapons#AR)",
                    inline=False)
    embed.add_field(name="Affinities",
                    value="Medium Ammo / Burn",
                    inline=True)
    embed.add_field(name="Weaknesses",
                    value="Heavy Ammo / Freeze",
                    inline=True)
    embed.add_field(name="Personality",
                    value="Resourcefulness",
                    inline=False)

    embed.set_image(url="https://iopwiki.com/images/thumb/e/ee/Qiongjiu_Whole.png/800px-Qiongjiu_Whole.png")

    embed.set_thumbnail(url="https://iopwiki.com/images/b/b1/Qiongjiu_S.png")

    embed.set_footer(text="Azure",
                    icon_url="https://cdn.discordapp.com/icons/1321437165774700575/ca4f95365bd06f8e9809c359185acc0d.webp")

    return embed

def get_mosin():
    embed = discord.Embed(title="Mosin-Nagant",
                      url="https://iopwiki.com/wiki/Mosin-Nagant_(GFL2)",
                      colour=0xf40068)

    embed.set_author(name="IOP Wiki",
                    url="https://iopwiki.com/",
                    icon_url="https://iopwiki.com/favicon.ico")

    embed.add_field(name="Rarity",
                    value="Elite",
                    inline=True)
    embed.add_field(name="Affiliation",
                    value="POL-03 Security Division",
                    inline=True)
    embed.add_field(name="Body type",
                    value="SST-05",
                    inline=False)
    embed.add_field(name="Role",
                    value="Sentinel",
                    inline=True)
    embed.add_field(name="Speciality",
                    value="Single Target Burst / Assist / Control",
                    inline=False)
    embed.add_field(name="Signature Weapon",
                    value="Mosin-Nagant",
                    inline=True)
    embed.add_field(name="Weapon Type",
                    value="RF",
                    inline=True)
    embed.add_field(name="Imprint Boost",
                    value="[Samosek](https://iopwiki.com/wiki/GFL2_Weapons#RF)",
                    inline=False)
    embed.add_field(name="Affinities",
                    value="Heavy Ammo / Electric",
                    inline=True)
    embed.add_field(name="Weaknesses",
                    value="Light Ammo / Corrosion",
                    inline=True)
    embed.add_field(name="Personality",
                    value="Eloquence",
                    inline=False)

    embed.set_image(url="https://iopwiki.com/images/thumb/3/39/Mosinnagant_Whole.png/1280px-Mosinnagant_Whole.png")

    embed.set_thumbnail(url="https://iopwiki.com/images/thumb/d/d3/Mosin-Nagant_%28GFL2%29_S.png/250px-Mosin-Nagant_%28GFL2%29_S.png")

    embed.set_footer(text="Azure",
                    icon_url="https://cdn.discordapp.com/icons/1321437165774700575/ca4f95365bd06f8e9809c359185acc0d.webp")

    return embed
