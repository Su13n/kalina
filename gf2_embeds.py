import discord

# Example template dict with keys matching what get_embed needs:
DOLL_DATA = {
    "sabrina": {
        "name": "Sabrina",
        "iop_url": "https://iopwiki.com/wiki/Sabrina",
        "rarity": "Elite",
        "affiliation": "Caldo Italian Restaurants",
        "body_type": "SSD-62D",
        "role": "Bulwark",
        "specialty": " 	Stability Defense / Counterattack / Tile ",
        "signature": "SPAS-12",
        "weapon_type": "SG",
        "imprint_name": "Mezzaluna",
        "affinity": "Shotgun Ammo / Hydro",
        "weakness": "Heavy Ammo / Electric",
        "personality": "Friendliness",
        "thumbnail": "https://iopwiki.com/images/3/3a/Sabrina_S.png"
    },
    "suomi": {
        "name": "Suomi",
        "iop_url": "https://iopwiki.com/wiki/Suomi_(GFL2)",
        "rarity": "Elite",
        "affiliation": "Doll Community",
        "body_type": "SSD-62D",
        "role": "Support",
        "specialty": "Heal & Stability Regen / Shield",
        "signature": "Suomi KP-31",
        "weapon_type": "SMG",
        "imprint_name": "Unspoken Calling",
        "affinity": "Light Ammo / Freeze",
        "weakness": "Heavy Ammo / Corrosion",
        "personality": "Friendliness",
        "thumbnail": "https://iopwiki.com/images/3/3a/Suomi_%28GFL2%29_S.png"
    },
    "tololo": {
        "name": "Tololo",
        "iop_url": "https://iopwiki.com/wiki/Tololo",
        "rarity": "Elite",
        "affiliation": 'G&K "Frostfall" Team',
        "body_type": "SST-05",
        "role": "Sentinel",
        "specialty": "Single Target Burst / Extra Action",
        "signature": "AK-Alfa ",
        "weapon_type": "AR",
        "imprint_name": "Planeta",
        "affinity": "Medium Ammo / Hydro",
        "weakness": "Heavy Ammo / Electric",
        "personality": "Creativity",
        "thumbnail": "https://iopwiki.com/images/4/49/Tololo_S.png"
    },
    "papasha": {
        "name": "Papasha",
        "iop_url": "https://iopwiki.com/wiki/Papasha",
        "rarity": "Elite",
        "affiliation": "[Elmo](https://iopwiki.com/wiki/Elmo) - POL-03 Security Division",
        "body_type": "SSD-62G",
        "role": "Sentinel",
        "specialty": "Single Target Burst / Summon",
        "signature": "PPSh-41",
        "weapon_type": "SMG",
        "imprint_name": "Svarog",
        "affinity": "Light Ammo",
        "weakness": "Shotgun Ammo / Corrosion",
        "personality": "Friendliness",
        "thumbnail": "https://iopwiki.com/images/c/cc/Papasha_S.png"
    },
    "peritya": {
        "name": "Peritya",
        "iop_url": "https://iopwiki.com/wiki/Peritya",
        "rarity": "Elite",
        "affiliation": "None",
        "body_type": "SSD-62D",
        "role": "Sentinel",
        "specialty": "Wide Area / Team Support / Displacement",
        "signature": "PKP-SP GPMG",
        "weapon_type": "MG",
        "imprint_name": "Optical Illusion",
        "affinity": "Heavy Ammo / Corrosion",
        "weakness": "Light Ammo / Hydro",
        "personality": "Creativity",
        "thumbnail": "https://iopwiki.com/images/3/30/Peritya_S.png"
    },
    "ullrid": {
        "name": "Ullrid",
        "iop_url": "https://iopwiki.com/wiki/Ullrid",
        "rarity": "Elite",
        "affiliation": "Doll Community",
        "body_type": "SST-62G",
        "role": "Vanguard",
        "specialty": "Melee Damage / Combo Attack / Stealth",
        "signature": "Pluma Edge",
        "weapon_type": "BLD",
        "imprint_name": "Rectrix",
        "affinity": "Melee / Light Ammo",
        "weakness": "Heavy Ammo / Freeze",
        "personality": "Courage",
        "thumbnail": "https://iopwiki.com/images/9/9b/Ullrid_S.png"
    },
    "": {
        "name": "",
        "iop_url": "https://iopwiki.com/wiki/",
        "rarity": "Elite",
        "affiliation": "",
        "body_type": "",
        "role": "",
        "specialty": "",
        "signature": "",
        "weapon_type": "",
        "imprint_name": "",
        "affinity": "",
        "weakness": "",
        "personality": "",
        "thumbnail": ""
    },
    "makiatto": {
        "name": "Makiatto",
        "iop_url": "https://iopwiki.com/wiki/Makiatto",
        "rarity": "Elite",
        "affiliation": "Zucchero Café",
        "body_type": "SSD-62D",
        "role": "Sentinel",
        "specialty": "Single Target Damage / First Strike",
        "signature": "WA2000",
        "weapon_type": "RF",
        "imprint_name": "Bittersweet Caramel",
        "affinity": "Heavy Ammo / Freeze",
        "weakness": "Light Ammo / Burn",
        "personality": "Courage",
        "thumbnail": "https://iopwiki.com/images/a/a9/Makiatto_S.png"
    },
    "qiongjiu": {
        "name": "Qiongjiu",
        "iop_url": "https://iopwiki.com/wiki/Qiongjiu",
        "rarity": "Elite",
        "affiliation": "G&K \"Frostfall\" Team",
        "body_type": "SSD-62G",
        "role": "Sentinel",
        "specialty": "Sustained Damage / Assist",
        "signature": "QBZ-191",
        "weapon_type": "AR",
        "imprint_name": "Golden Melody",
        "affinity": "Medium Ammo / Burn",
        "weakness": "Heavy Ammo / Freeze",
        "personality": "Resourcefulness",
        "thumbnail": "https://iopwiki.com/images/b/b1/Qiongjiu_S.png"
    },
    "mosin": {
        "name": "Mosin-Nagant",
        "iop_url": "https://iopwiki.com/wiki/Mosin-Nagant_(GFL2)",
        "rarity": "Elite",
        "affiliation": "POL-03 Security Division",
        "body_type": "SST-05",
        "role": "Sentinel",
        "specialty": "Single Target Burst / Assist / Control",
        "signature": "Mosin-Nagant",
        "weapon_type": "RF",
        "imprint_name": "Samosek",
        "affinity": "Heavy Ammo / Electric",
        "weakness": "Light Ammo / Corrosion",
        "personality": "Eloquence",
        "thumbnail": "https://iopwiki.com/images/thumb/d/d3/Mosin-Nagant_%28GFL2%29_S.png/250px-Mosin-Nagant_%28GFL2%29_S.png"
    },
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
    "andoris": {
        "name": "Andoris",
        "iop_url": "https://iopwiki.com/wiki/Andoris",
        "rarity": "Elite",
        "affiliation": "H.I.D.E 404",
        "body_type": "SST-62F",
        "role": "Bulwark",
        "specialty": "?",
        "signature": "G36-KSK",
        "weapon_type": "AR",
        "imprint_name": "Aglaea",
        "affinity": "Medium Ammo / Electric",
        "weakness": "Heavy Ammo / Corrosion",
        "personality": "?",
        "thumbnail": "https://iopwiki.com/images/9/91/Andoris_S.png"
    },
    "vepley": {
        "name": "Vepley",
        "iop_url": "https://iopwiki.com/wiki/Vepley",
        "rarity": "Elite",
        "affiliation": "[Elmo](https://iopwiki.com/wiki/Elmo) MCV",
        "body_type": "SSD-62D",
        "role": "Vanguard",
        "specialty": "Mixed Damage / Debuff / Displacement",
        "signature": "Vepr-12",
        "weapon_type": "SG",
        "imprint_name": "Heart Seeker",
        "affinity": "Shotgun Ammo",
        "weakness": "Heavy Ammo / Hydro",
        "personality": "Friendliness",
        "thumbnail": "https://iopwiki.com/images/thumb/5/52/Vepley_S.png"
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
    "cheeta": {
        "name": "Cheeta",
        "iop_url": "https://iopwiki.com/wiki/Cheeta",
        "rarity": "Standard",
        "affiliation": 'G&K "Frostfall" Team',
        "body_type": "SSD-62D",
        "role": "Support",
        "specialty": "Random Buff / Assist / Heal",
        "signature": "MP7",
        "weapon_type": "SMG",
        "imprint_name": "None",
        "affinity": "Light Ammo / Burn",
        "weakness": "Medium Ammo / Hydro",
        "personality": "Creativity",
        "thumbnail": "https://iopwiki.com/images/5/59/Cheeta_S.png"
    },
    "colphne": {
        "name": "Colphne",
        "iop_url": "https://iopwiki.com/wiki/Colphne",
        "rarity": "Standard",
        "affiliation": "[Elmo](https://iopwiki.com/wiki/Elmo) MCV",
        "body_type": "SSD-62D",
        "role": "Support",
        "specialty": "Heal & Stability Regen / Assist",
        "signature": "Taurus Curva",
        "weapon_type": "HG",
        "imprint_name": "None",
        "affinity": "Light Ammo / Hydro",
        "weakness": "Shotgun Ammo / Corrosion",
        "personality": "Friendliness",
        "thumbnail": "https://iopwiki.com/images/6/68/Colphne_S.png"
    },
    "groza": {
        "name": "Groza",
        "iop_url": "https://iopwiki.com/wiki/Groza",
        "rarity": "Standard",
        "affiliation": "[Elmo](https://iopwiki.com/wiki/Elmo) MCV",
        "body_type": "SST-05A2",
        "role": "Bulwark",
        "specialty": "Stability Defense / Counterattack",
        "signature": "OTs-14",
        "weapon_type": "AR",
        "imprint_name": "None",
        "affinity": "Medium Ammo",
        "weakness": "Heavy Ammo / Burn",
        "personality": "Courage",
        "thumbnail": "https://iopwiki.com/images/3/3e/Groza_S.png"
    },
    "krolik": {
        "name": "Krolik",
        "iop_url": "https://iopwiki.com/wiki/Krolik",
        "rarity": "Standard",
        "affiliation": "[Elmo](https://iopwiki.com/wiki/Elmo) MCV",
        "body_type": "SSD-62D",
        "role": "Vanguard",
        "specialty": "Melee Damage / Debuff",
        "signature": "Hare",
        "weapon_type": "BLD",
        "imprint_name": "None",
        "affinity": "Melee / Burn",
        "weakness": "Shotgun Ammo / Corrosion",
        "personality": "Courage",
        "thumbnail": "https://iopwiki.com/images/8/84/Krolik_S.png"
    },
    "ksenia": {
        "name": "",
        "iop_url": "https://iopwiki.com/wiki/Ksenia",
        "rarity": "Standard",
        "affiliation": "POL-03 Security Division",
        "body_type": "SSD-62D ",
        "role": "Support",
        "specialty": "Heal & Stability Regen / Buff",
        "signature": "Stechkin",
        "weapon_type": "HG",
        "imprint_name": "None",
        "affinity": "Light Ammo / Burn",
        "weakness": "Medium Ammo / Burn",
        "personality": "Eloquence",
        "thumbnail": "https://iopwiki.com/images/f/f5/Ksenia_%28GFL2%29_S.png"
    },
    "littara": {
        "name": "Littara",
        "iop_url": "https://iopwiki.com/wiki/Littara",
        "rarity": "Standard",
        "affiliation": "[][][][]",
        "body_type": "SSD-62G ",
        "role": "Sentinel",
        "specialty": "AoE Damage / Pursuit",
        "signature": " 	Galil ARM ",
        "weapon_type": "MG",
        "imprint_name": "None",
        "affinity": "Heavy Ammo / Burn",
        "weakness": "Light Ammo / Burn",
        "personality": "Resourcefullness",
        "thumbnail": "https://iopwiki.com/images/4/4e/Littara_S.png"
    },
    "lotta": {
        "name": "Lotta",
        "iop_url": "https://iopwiki.com/wiki/Lotta",
        "rarity": "Standard",
        "affiliation": "Doll Community",
        "body_type": "SSD-62D",
        "role": "Sentinel",
        "specialty": "AoE Damage / Debuff / Assist",
        "signature": "M1 Super 90",
        "weapon_type": "SG",
        "imprint_name": "None",
        "affinity": "Shotgun Ammo / Freeze",
        "weakness": "Medium Ammo / Burn",
        "personality": "Resourcefullness",
        "thumbnail": "https://iopwiki.com/images/3/3b/Lotta_S.png"
    },
    "nemesis": {
        "name": "Nemesis",
        "iop_url": "https://iopwiki.com/wiki/",
        "rarity": "Standard",
        "affiliation": "[Elmo](https://iopwiki.com/wiki/Elmo) MCV",
        "body_type": "SST-05A2",
        "role": "Sentinel",
        "specialty": "Single Target Damage / Assist",
        "signature": "OM 50/SAN 511",
        "weapon_type": "RF",
        "imprint_name": "None",
        "affinity": "Heavy Ammo / Corrosion",
        "weakness": "Light Ammo / Hydro",
        "personality": "Creativity",
        "thumbnail": "https://iopwiki.com/images/3/37/Nemesis_S.png"
    }
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