from discord import Embed


async def infos(message):
    await message.delete()
    member = message.mentions[0]
    embed = Embed(
        title=f"🛈 __**Informations sur {member.name} :**__",
        url="http://www.nymeria.org/",
        description="",
        color=0xF7AF00,
    )
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.add_field(name="**Member ID :**", value=f"{member.id}", inline=True)
    embed.add_field(
        name="**Création du compte :**",
        value=f"{member.created_at.day}-{member.created_at.month}-{member.created_at.year} {member.created_at.hour}:{member.created_at.minute}:{member.created_at.second}",
        inline=True,
    )
    for guildMember in message.guild.members:
        if guildMember == member:
            embed.add_field(
                name="**A rejoint :**",
                value=f"{guildMember.joined_at.day}-{guildMember.joined_at.month}-{guildMember.joined_at.year} {guildMember.joined_at.hour}:{guildMember.joined_at.minute}:{guildMember.joined_at.second}",
                inline=True,
            )
    await message.channel.send(embed=embed)
