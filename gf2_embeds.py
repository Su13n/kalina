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

    embed.set_image(url="https://iopwiki.com/images/3/33/Macqiato_Whole.png")

    embed.set_thumbnail(url="https://iopwiki.com/images/a/a9/Makiatto_S.png")

    embed.set_footer(text="Azure",
                    icon_url="https://cdn.discordapp.com/icons/1321437165774700575/ca4f95365bd06f8e9809c359185acc0d.webp")

    return embed