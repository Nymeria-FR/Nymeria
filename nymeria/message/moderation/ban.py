from nymeria.utility import get_guild
import discord

async def ban(message):
    await message.delete()
    commande = message.content.split(" ")
    if message.author.guild_permissions.ban_members is False:
        await message.channel.send(
            "{}\nTu ne peux pas ban ".format(message.author.mention)
            + "cet utilisateur"
        )
        return
    if len(commande) == 2:
        try:
            ban = message.mentions[0]
            await message.guild.ban(ban)
            embedVar = discord.Embed(
                title=f"__**{ban.name} a été ban**__",
                url="http://www.nymeria.org/",
                description=message.author.mention
                + "\nL'utilisateur a bien été ban 🔨",
                color=0xF7AF00
            )
            embedVar.set_thumbnail(url=f"{ban.avatar_url}")
            await message.channel.send(embed=embedVar)
            # await message.channel.send("{}\n L'utilisateur a bien été ban".format(message.author.mention))
        except discord.HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas ban ".format(message.author.mention)
                + "cet utilisateur"
            )
        except discord.Forbidden:
            await message.channel.send(
                "{}\n Je ne peux pas ban ".format(message.author.mention)
                + "cet utilisateur"
            )
    if len(commande) >= 3:
        try:
            ban = message.mentions[0]
            guild = get_guild(861292008101642281)
            await message.guild.ban(ban, reason=" ".join(commande[2:]))

            embedVar = discord.Embed(
                title=f"__**{ban.name} a été ban**__",
                url="http://www.nymeria.org/",
                description=message.author.mention
                + "\nL'utilisateur a bien été ban 🔨\nRaison : "
                + " ".join(commande[2:]),
                color=0xF7AF00
            )
            embedVar.set_thumbnail(url=f"{ban.avatar_url}")
            await message.channel.send(embed=embedVar)

            # await message.channel.send("{}\n L'utilisateur a bien été ban".format(message.author.mention))
        except discord.HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas ban ".format(message.author.mention)
                + "cet utilisateur"
            )
        except discord.Forbidden:
            await message.channel.send(
                "{}\n Je ne peux pas ban ".format(message.author.mention)
                + "cet utilisateur"
            )
    return

async def unban(message):
    await message.delete()
    commande = message.content.split(" ")
    if message.author.guild_permissions.ban_members is False:
        await message.channel.send(
            "{}\n Je ne peux pas deban ".format(message.author.mention)
            + "cet utilisateur"
        )
        return
    if len(commande) >= 2:
        try:
            ban = discord.Object(commande[1])
            bans = await message.guild.bans()
            user = None
            for banned in bans:
                if banned.user.id == ban.id:
                    user = banned.user
            #user = await message.guild.fetch_user(commande[1])
            await message.guild.unban(ban)
            embedVar = discord.Embed(
                title=f"__**{user.name} a été unban**__",
                url="http://www.nymeria.org/",
                description=message.author.mention
                + "\nL'utilisateur a bien été unban ✅",
                color=0xF7AF00
            )
            embedVar.set_thumbnail(url=f"{user.avatar_url}")
            await message.channel.send(embed=embedVar)
            # await message.channel.send("{}\n L'utilisateur a bien été unban".format(message.author.mention))
        except discord.HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas deban ".format(message.author.mention)
                + "cet utilisateur"
            )
        except discord.Forbidden:
            await message.channel.send(
                "{}\n Je ne peux pas deban ".format(message.author.mention)
                + "cet utilisateur"
            )
    return

async def kick(message):
    await message.delete()
    commande = message.content.split(" ")
    if message.author.guild_permissions.kick_members is False:
        await message.channel.send(
            "{}\n Tu ne peux pas kick ".format(message.author.mention)
            + "cet utilisateur"
        )
        return
    if len(commande) >= 2:
        try:
            mention = message.mentions[0]
            await message.guild.kick(mention)
            embedVar = discord.Embed(
                title=f"__**{mention.name} a été kick**__",
                url="http://www.nymeria.org/",
                description=message.author.mention
                + "\nL'utilisateur a bien été kick 🔨",
                color=0xF7AF00
            )
            embedVar.set_thumbnail(url=f"{mention.avatar_url}")
            await message.channel.send(embed=embedVar)
            # await message.channel.send("{}\n L'utilisateur a bien été kick".format(message.author.mention))
        except discord.HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas kick ".format(message.author.mention)
                + "cet utilisateur"
            )
        except discord.Forbidden:
            await message.channel.send(
                "{}\n Je ne peux pas kick ".format(message.author.mention)
                + "cet utilisateur"
            )
    return

async def banlist(message):
    bans = await message.guild.bans()
    des = ""
    for banned in bans:
        if banned.reason == None:
            des += (
                banned.user.name
                + "#"
                + str(banned.user.discriminator)
                + " **("
                + str(banned.user.id)
                + ")** | `Raison : pas spécifiée`\n"
            )
        else:
            des += (
                banned.user.name
                + "#"
                + str(banned.user.discriminator)
                + " **("
                + str(banned.user.id)
                + ")** | `Raison : "
                + banned.reason
                + "`\n"
            )

    embedVar = discord.Embed(
        title="__**Ban List**__ 🔨",
        url="http://www.nymeria.org/",
        description=des,
        color=0xF7AF00
    )
    await message.channel.send(embed=embedVar)