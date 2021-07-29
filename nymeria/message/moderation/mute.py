from discord import HTTPException, Forbidden, Embed
import asyncio


async def mute(message):
    await message.delete()
    guild = message.guild
    if guild.id == 558023940518313987:
        for role in guild.roles:
            if role.id == 755909610803560559:
                mute_role = role

    commande = message.content.split(" ")
    if message.author.guild_permissions.kick_members is False:
        await message.channel.send(
            "{}\n Tu ne peux pas mute ".format(message.author.mention)
            + "cet utilisateur"
        )
        return
    if len(commande) == 2:
        try:
            mention = message.mentions[0]
            await mention.add_roles(mute_role)
            embedVar = Embed(
                title=f"__**{mention.name} a été mute**__",
                url="http://www.nymeria.org/",
                description=mention.mention + "\nTu as été mute ⛔",
                color=0xF7AF00,
            )
            embedVar.set_thumbnail(url=f"{mention.avatar_url}")
            await message.channel.send(embed=embedVar)

        except HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas mute ".format(message.author.mention)
                + "cet utilisateur"
            )

        except Forbidden:
            await message.channel.send(
                "{}\n Je ne peux pas mute ".format(message.author.mention)
                + "cet utilisateur"
            )
    if len(commande) == 3:
        try:
            mention = message.mentions[0]
            await mention.add_roles(mute_role)
            embedVar = Embed(
                title=f"__**{mention.name} a été mute**__",
                url="http://www.nymeria.org/",
                description=mention.mention
                + "\n Tu as été mute pour "
                + commande[2]
                + " secondes ⛔",
                color=0xF7AF00,
            )

            embedVar.set_thumbnail(url=f"{mention.avatar_url}")
            await message.channel.send(embed=embedVar)
            await asyncio.sleep(int(commande[2]))
            await mention.remove_roles(mute_role)
            embedVar = Embed(
                title=f"__**{mention.name} a été unmute**__",
                description=mention.mention + "\nTu peux de nouveau parler ✅",
                color=0xF7AF00,
            )

            embedVar.set_thumbnail(url=f"{mention.avatar_url}")
            await message.channel.send(embed=embedVar)

        except HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas mute ".format(message.author.mention)
                + "cet utilisateur"
            )

        except Forbidden:
            await message.channel.send(
                "{}\n Je ne peux pas mute ".format(message.author.mention)
                + "cet utilisateur"
            )
    return


async def unmute(message):
    await message.delete()
    guild = message.guild
    if guild.id == 558023940518313987:
        for role in guild.roles:
            if role.id == 755909610803560559:
                mute_role = role

    commande = message.content.split(" ")
    if message.author.guild_permissions.kick_members is False:
        await message.channel.send(
            "{}\n Tu ne peux pas unmute ".format(message.author.mention)
            + "cet utilisateur"
        )
        return
    if len(commande) >= 2:
        try:
            mention = message.mentions[0]
            await mention.remove_roles(mute_role)
            embedVar = Embed(
                title=f"__**{mention.name} a été unmute**__",
                url="http://www.nymeria.org/",
                description=mention.mention + "\nTu peux de nouveau parler ✅",
                color=0xF7AF00,
            )
            embedVar.set_thumbnail(url=f"{mention.avatar_url}")
            await message.channel.send(embed=embedVar)

        except HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas unmute ".format(message.author.mention)
                + "cet utilisateur"
            )

        except Forbidden:
            await message.channel.send(
                "{}\n Je ne peux pas unmute ".format(message.author.mention)
                + "cet utilisateur"
            )
    return
