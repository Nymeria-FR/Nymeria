from nymeria.utility import get_guild
from discord import Embed, HTTPException, Forbidden, Object


async def ban(message):
    await message.delete()
    commande = message.content.split(" ")
    if message.author.guild_permissions.ban_members is False:
        await message.channel.send(
            "{}\nTu ne peux pas ban ".format(message.author.mention)
            + "cet utilisateur"
        )
        return
    try:
        if len(commande) == 2:
            ban = message.mentions[0]
            await message.guild.ban(ban)
        elif len(commande) >= 3:
            ban = message.mentions[0]
            await message.guild.ban(ban, reason=" ".join(commande[2:]))

        embedVar = Embed(
            title=f"__**{ban.name} a été ban**__",
            url="http://www.nymeria.org/",
            description=message.author.mention
            + "\nL'utilisateur a bien été ban 🔨",
            color=0xF7AF00
        )
        embedVar.set_thumbnail(url=f"{ban.avatar_url}")
        await message.channel.send(embed=embedVar)

    except HTTPException:
        await message.channel.send(
            "{}\n Je ne peux pas ban ".format(message.author.mention)
            + "cet utilisateur"
        )

    except Forbidden:
        await message.channel.send(
            "{}\n Je ne peux pas ban ".format(message.author.mention)
            + "cet utilisateur"
        )


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
            ban = Object(commande[1])
            bans = await message.guild.bans()
            user = None
            for banned in bans:
                if banned.user.id == ban.id:
                    user = banned.user
            await message.guild.unban(ban)
            embedVar = Embed(
                title=f"__**{user.name} a été unban**__",
                url="http://www.nymeria.org/",
                description=message.author.mention
                + "\nL'utilisateur a bien été unban ✅",
                color=0xF7AF00
            )
            embedVar.set_thumbnail(url=f"{user.avatar_url}")
            await message.channel.send(embed=embedVar)
        except HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas deban ".format(message.author.mention)
                + "cet utilisateur"
            )
        except Forbidden:
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
            embedVar = Embed(
                title=f"__**{mention.name} a été kick**__",
                url="http://www.nymeria.org/",
                description=message.author.mention
                + "\nL'utilisateur a bien été kick 🔨",
                color=0xF7AF00
            )
            embedVar.set_thumbnail(url=f"{mention.avatar_url}")
            await message.channel.send(embed=embedVar)

        except HTTPException:
            await message.channel.send(
                "{}\n Je ne peux pas kick ".format(message.author.mention)
                + "cet utilisateur"
            )

        except Forbidden:
            await message.channel.send(
                "{}\n Je ne peux pas kick ".format(message.author.mention)
                + "cet utilisateur"
            )
    return


async def banlist(message):
    bans = await message.guild.bans()
    des = ""
    for banned in bans:
        des += (
            banned.user.name
            + "#"
            + str(banned.user.discriminator)
            + " **("
            + str(banned.user.id)
            + ")** | `Raison : " + ("pas spécifiée" if (banned.reason == None) else banned.reason)  + "`\n"
        )

    embedVar = Embed(
        title="__**Ban List**__ 🔨",
        url="http://www.nymeria.org/",
        description=des,
        color=0xF7AF00
    )
    await message.channel.send(embed=embedVar)


async def ban_analyse(message):
    if message.content.startswith("n!banlist"):
        await banlist(message)
        return True

    elif message.content.startswith("n!ban"):
        await ban(message)
        return True

    elif message.content.startswith("n!ub"):
        await unban(message)
        return True

    elif message.content.startswith("n!kick"):
        await kick(message)
        return True
    
    return False