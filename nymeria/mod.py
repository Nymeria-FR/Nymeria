import discord
import datetime
from pytz import timezone
from asyncio import sleep


class Moderation:

    async def deleteMessage(self, message):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        if message.author.guild_permissions.manage_messages is True:
            await message.channel.delete_messages(messages)
            return
        await message.channel.send(
            f"""{message.author.mention}
Tu ne peux pas suprimer de message"""
        )

    async def add_bot_role(self, member):
        if member.bot is True:
            guild = self.get_guild(861292008101642281)
            bot = guild.get_role(861292008101642286)
            await member.add_roles(bot)
            return True
        return False

    async def add_member_role(self, member):
        for guild in self.guilds:
            if guild.id == 861292008101642281:
                for role in guild.roles:
                    if role.id == 861292008101642287:
                        member_role = role
        await member.add_roles(member_role)

    async def ban(self, message):
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
                    url = "http://www.nymeria.org/",
                    description=message.author.mention + "\nL'utilisateur a bien été ban 🔨",
                    color=0xF7AF00,
                    timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
                )
                embedVar.set_thumbnail(url=f'{ban.avatar_url}')
                await message.channel.send(embed=embedVar)
                #await message.channel.send("{}\n L'utilisateur a bien été ban".format(message.author.mention))
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
                guild = self.get_guild(861292008101642281)
                await message.guild.ban(ban,reason=" ".join(commande[2:]))

                embedVar = discord.Embed(
                    title=f"__**{ban.name} a été ban**__",
                    url = "http://www.nymeria.org/",
                    description=message.author.mention + "\nL'utilisateur a bien été ban 🔨\nRaison : " + " ".join(commande[2:]),
                    color=0xF7AF00,
                    timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
                )
                embedVar.set_thumbnail(url=f'{ban.avatar_url}')
                await message.channel.send(embed=embedVar)
                
                #await message.channel.send("{}\n L'utilisateur a bien été ban".format(message.author.mention))
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

    async def unban(self, message):
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
                user = await self.fetch_user(commande[1])
                await message.guild.unban(ban)
                embedVar = discord.Embed(
                    title=f"__**{user.name} a été unban**__",
                    url = "http://www.nymeria.org/",
                    description=message.author.mention + "\nL'utilisateur a bien été unban ✅",
                    color=0xF7AF00,
                    timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
                )
                embedVar.set_thumbnail(url=f'{user.avatar_url}')
                await message.channel.send(embed=embedVar)
                #await message.channel.send("{}\n L'utilisateur a bien été unban".format(message.author.mention))
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

    async def kick(self, message):
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
                    url = "http://www.nymeria.org/",
                    description=message.author.mention + "\nL'utilisateur a bien été kick 🔨",
                    color=0xF7AF00,
                    timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
                )
                embedVar.set_thumbnail(url=f'{mention.avatar_url}')
                await message.channel.send(embed=embedVar)
                #await message.channel.send("{}\n L'utilisateur a bien été kick".format(message.author.mention))
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
    
    async def mute(self,message):
        await message.delete()
        for guild in self.guilds:
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
                embedVar = discord.Embed(
                    title=f"__**{mention.name} a été mute**__",
                    url = "http://www.nymeria.org/",
                    description=mention.mention + "\nTu as été mute ⛔",
                    color=0xF7AF00,
                    timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
                )
                embedVar.set_thumbnail(url=f'{mention.avatar_url}')
                await message.channel.send(embed=embedVar)
                #await message.channel.send("{} Tu as été mute".format(mention.mention))
            except discord.HTTPException:
                await message.channel.send(
                    "{}\n Je ne peux pas mute ".format(message.author.mention)
                    + "cet utilisateur"
                )
            except discord.Forbidden:
                await message.channel.send(
                    "{}\n Je ne peux pas mute ".format(message.author.mention)
                    + "cet utilisateur"
                )
        if len(commande) == 3:
            try:
                mention = message.mentions[0]
                await mention.add_roles(mute_role)
                embedVar = discord.Embed(
                    title=f"__**{mention.name} a été mute**__",
                    url = "http://www.nymeria.org/",
                    description=mention.mention + "\n Tu as été mute pour " + commande[2] + " secondes ⛔",
                    color=0xF7AF00,
                    timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
                )
                embedVar.set_thumbnail(url=f'{mention.avatar_url}')
                await message.channel.send(embed=embedVar)
                #await message.channel.send("{} est mute pour {} secondes".format(mention.mention,commande[2]))
                await sleep(int(commande[2]))
                await mention.remove_roles(mute_role)
                embedVar = discord.Embed(
                    title=f"__**{mention.name} a été unmute**__",
                    description=mention.mention + "\nTu peux de nouveau parler ✅",
                    color=0xF7AF00,
                    timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
                )
                embedVar.set_thumbnail(url=f'{mention.avatar_url}')
                await message.channel.send(embed=embedVar)
                #await message.channel.send("{} Tu peux de nouveau parler".format(mention.mention))
            except discord.HTTPException:
                await message.channel.send(
                    "{}\n Je ne peux pas mute ".format(message.author.mention)
                    + "cet utilisateur"
                )
            except discord.Forbidden:
                await message.channel.send(
                    "{}\n Je ne peux pas mute ".format(message.author.mention)
                    + "cet utilisateur"
                )
        return


    async def unmute(self,message):
        await message.delete()
        for guild in self.guilds:
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
                #print(", ".join([str(r.id) for r in mention.roles]))
                embedVar = discord.Embed(
                    title=f"__**{mention.name} a été unmute**__",
                    url = "http://www.nymeria.org/",
                    description=mention.mention + "\nTu peux de nouveau parler ✅",
                    color=0xF7AF00,
                    timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
                )
                embedVar.set_thumbnail(url=f'{mention.avatar_url}')
                await message.channel.send(embed=embedVar)
                #await message.channel.send("{} Tu peux de nouveau parler".format(mention.mention))
            except discord.HTTPException:
                await message.channel.send(
                    "{}\n Je ne peux pas unmute ".format(message.author.mention)
                    + "cet utilisateur"
                )
            except discord.Forbidden:
                await message.channel.send(
                    "{}\n Je ne peux pas unmute ".format(message.author.mention)
                    + "cet utilisateur"
                )
        return

    async def banlist(self,message):
        idy = message.guild.id
        guild = self.get_guild(idy)
        bans = await guild.bans()

        date = datetime.datetime.now(timezone("Europe/Berlin"))
        des = ""
        for banned in bans:
            if banned.reason == None:
                des += banned.user.name + '#' + str(banned.user.discriminator) + ' **(' + str(banned.user.id) + ")** | `Raison : pas spécifiée`\n"
            else: des += banned.user.name + '#' + str(banned.user.discriminator) + ' **(' + str(banned.user.id) + ")** | `Raison : " + banned.reason + "`\n"
        
        embedVar = discord.Embed(
            title="__**Ban List**__ 🔨",
            url = "http://www.nymeria.org/",
            description=des,
            color=0xF7AF00,
            timestamp=date,
        )
        await message.channel.send(embed=embedVar)

    async def infos(self,message):
        await message.delete()
        member = message.mentions[0]
        embed = discord.Embed(title=f"🛈 __**Informations sur {member.name} :**__", url = "http://www.nymeria.org/", description="", color=0xF7AF00)
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.add_field(name="**Member ID :**", value=f"{member.id}", inline=True)
        embed.add_field(name="**Création du compte :**", value=f"{member.created_at.day}-{member.created_at.month}-{member.created_at.year} {member.created_at.hour}:{member.created_at.minute}:{member.created_at.second}", inline=True)
        for guildMember in message.guild.members:
            if guildMember == member:
                embed.add_field(name="**A rejoint :**", value=f"{guildMember.joined_at.day}-{guildMember.joined_at.month}-{guildMember.joined_at.year} {guildMember.joined_at.hour}:{guildMember.joined_at.minute}:{guildMember.joined_at.second}", inline=True)
        await message.channel.send(embed=embed)
    
    async def ban_word(self,message):
        await message.delete()
        embedVar = discord.Embed(
            title="__**Warning**__ ⚠",
            url = "http://www.nymeria.org/",
            description=f"{message.author.mention} \nAttention, tu as utilisé un mot interdit",
            color=0xF7AF00,
            timestamp=datetime.datetime.now(timezone("Europe/Berlin")),
        )
        embedVar.set_thumbnail(url=f'{message.author.avatar_url}')
        await message.channel.send(embed=embedVar)

    async def emote(self, message):
        commande = message.content.split(" ")
        for emo in commande[1:]:
            if emo[0] != ":" and emo[-1] != ":":
                await message.delete()
