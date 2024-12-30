import discord

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

    embed.set_thumbnail(url="https://iopwiki.com/images/9/91/Andoris_S.png")

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

    embed.set_thumbnail(url="https://iopwiki.com/images/thumb/d/d3/Mosin-Nagant_%28GFL2%29_S.png/250px-Mosin-Nagant_%28GFL2%29_S.png")

    embed.set_footer(text="Azure",
                    icon_url="https://cdn.discordapp.com/icons/1321437165774700575/ca4f95365bd06f8e9809c359185acc0d.webp")

    return embed

# Example template dict with keys matching what get_embed needs:
DOLL_DATA = {
    "klukai": {
        "name": "Clukay",
        "iop_url": "https://iopwiki.com/wiki/Klukai",
        "rarity": "Elite",
        "affiliation": "H.I.D.E 404",
        "body_type": "SST-05",
        "role": "Sentinel",
        "specialty": "?",
        "signature": "HK416",
        "weapon_type": "AR",
        "imprint_name": "Scylla",
        "affinity": "Medium Ammo / Corrosion",
        "weakness": "Shotgun Ammo / Electric",
        "personality": "?",
        "thumbnail": "https://iopwiki.com/images/thumb/1/11/Klukai_S.png/250px-Klukai_S.png"
    },
    "nagant": {
        "name": "Nagant",
        "iop_url": "https://iopwiki.com/wiki/Nagant",
        "rarity": "Standard",
        "affiliation": "POL-03 Public Security Management Department",
        "body_type": "SSD-62D",
        "role": "Support",
        "specialty": "Single Target Debuff / Pursuit",
        "signature": "Nagant M1895",
        "weapon_type": "HG",
        "imprint_name": "None",
        "affinity": "Light Ammo / Corrosion",
        "weakness": "Shotgun Ammo / Burn",
        "personality": "Eloquence",
        "thumbnail": "https://iopwiki.com/images/thumb/3/34/Nagant_S.png/250px-Nagant_S.png"
    },
    "sharkry": {
        "name": "Sharkry",
        "iop_url": "https://iopwiki.com/wiki/Sharkry",
        "rarity": "Standard",
        "affiliation": "Zucchero Café",
        "body_type": "SSD-62D",
        "role": "Sentinel",
        "specialty": "Single Target Damage / Debuff",
        "signature": "Robinson Armament XCR",
        "weapon_type": "AR",
        "imprint_name": "None",
        "affinity": "Medium  Ammo / Burn",
        "weakness": "Medium Ammo / Corrosiion",
        "personality": "Resourcefullness",
        "thumbnail": "https://iopwiki.com/images/e/e5/Sharkry_S.png"
    },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # },
    # "": {
    #     "name": "",
    #     "iop_url": "https://iopwiki.com/wiki/",
    #     "rarity": "Standard",
    #     "affiliation": "",
    #     "body_type": "",
    #     "role": "",
    #     "specialty": "",
    #     "signature": "",
    #     "weapon_type": "",
    #     "imprint_name": "",
    #     "affinity": "",
    #     "weakness": "",
    #     "personality": "",
    #     "thumbnail": ""
    # }
}

def get_embed(doll_name: str) -> discord.Embed:
    data = DOLL_DATA[doll_name]
    if not data:
        return None  # or handle error differently
    embed = discord.Embed(
        title=data["name"],
        url=data["iop_url"],
        colour=0xf40068
    )
    embed.set_author(
        name="IOP Wiki",
        url="https://iopwiki.com/",
        icon_url="https://iopwiki.com/favicon.ico"
    )
    embed.add_field(name="Rarity", value=data["rarity"], inline=True)
    embed.add_field(name="Affiliation", value=data["affiliation"], inline=True)
    embed.add_field(name="Body type", value=data["body_type"], inline=False)
    embed.add_field(name="Role", value=data["role"], inline=True)
    embed.add_field(name="Specialty", value=data["specialty"], inline=False)
    embed.add_field(name="Signature Weapon", value=data["signature"], inline=True)
    embed.add_field(name="Weapon Type", value=data["weapon_type"], inline=True)
    embed.add_field(
        name="Imprint Boost",
        value=f"[{data['imprint_name']}](https://iopwiki.com/wiki/GFL2_Weapons#{data['weapon_type']})",
        inline=False
    )
    embed.add_field(name="Affinities", value=data["affinity"], inline=True)
    embed.add_field(name="Weaknesses", value=data["weakness"], inline=True)
    embed.add_field(name="Personality", value=data["personality"], inline=False)

    embed.set_thumbnail(url=data["thumbnail"])
    embed.set_footer(
        text="Azure",
        icon_url="https://cdn.discordapp.com/icons/1321437165774700575/ca4f95365bd06f8e9809c359185acc0d.webp"
    )
    print("everything fine")
    return embed