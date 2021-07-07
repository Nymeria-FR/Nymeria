import json
import discord
import datetime

from pytz import timezone
from config import config


class Voice():
    def __init__(self):
        self.channelsid = []

    def load(self):
        f = open(config.data_base, "r")
        data = json.load(f)
        return data

    def save(self, data):
        with open(config.data_base, "w") as output:
            json.dump(data, output)

    async def voicEventTraitment(self, member, before, after):
        data = self.load()
        if (member.voice is not None and
                member.voice.channel.id == 861292010057105458):
            if str(member.id) not in data:
                data[str(member.id)] = [member.name + "'s channel", 0, None]

            category = member.voice.channel.category
            voiceCreate = await member.guild.create_voice_channel(
                data[str(member.id)][0],
                category=category)

            data[str(member.id)][1] = voiceCreate.id
            self.channelsid.append(data[str(member.id)][1])
            await member.move_to(voiceCreate)
            await voiceCreate.edit(user_limit=data[str(member.id)][2])
            await voiceCreate.set_permissions(member,
                                              connect=True,
                                              read_messages=True,
                                              manage_channels=True)

        elif (before.channel != after.channel and
              before.channel is not None):
            channelExit = self.get_channel(before.channel.id)
            if (channelExit.id != 861292010057105458 and
                channelExit.category_id == 861292009627844624 and
                    len(channelExit.members) == 0):
                await channelExit.delete()
            if str(member.id) in data:
                data[str(member.id)][1] = 0
        self.save(data)

    async def voiceCommande(self, message):
        if message.content == "n!voice lock":
            return await self.lock(message.author)
        elif message.content == "n!voice unlock":
            return await self.unlock(message.author)
        elif message.content == "n!voice claim":
            return await self.claim(message.author)
        elif message.content == "n!voice help":
            await self.commandes(message)
            return ""
        commande = message.content.split(" ")
        if len(commande) >= 3:
            if commande[1] == "name":
                return await self.rename(message.author, commande[2])
            elif commande[1] == "limit":
                return await self.limit(message.author, int(commande[2]))
            elif commande[1] == "permit" and message.mentions is not None:
                return await self.permit(message.author, message.mentions)
            elif commande[1] == "reject" and message.mentions is not None:
                return await self.reject(message.author, message.mentions)
        return "Cette commande n'existe pas"

    async def lock(self, member):
        data = self.load()
        print(data)
        if (str(member.id) in data and
                data[str(member.id)][1] != 0):
            channel = member.guild.get_channel(data[str(member.id)][1])
            role = member.guild.get_role(796356814421098547)
            await channel.set_permissions(role,
                                          connect=False,
                                          read_messages=True)
            return "{}\nLe channel a été bloqué 🔒".format(member.mention)

        return "{}\nTu ne possèdes pas de channel".format(member.mention)

    async def unlock(self, member):
        data = self.load()
        if (str(member.id) in data and
                data[str(member.id)][1] != 0):
            channel = member.guild.get_channel(data[str(member.id)][1])
            role = member.guild.get_role(796356814421098547)
            await channel.set_permissions(role,
                                          connect=True,
                                          read_messages=True)
            return "{}\nLe channel a été débloqué 🔓".format(member.mention)

        return "{}\nTu ne possèdes pas channel".format(member.mention)

    async def rename(self, member, name):
        data = self.load()
        if (str(member.id) in data and
                data[str(member.id)][1] != 0):
            channel = member.guild.get_channel(data[str(member.id)][1])
            await channel.edit(name=name)
            data[str(member.id)][0] = name
            self.save(data)
            return "{}\nLe nom du channel a été changé en {}".format(
                member.mention,
                name)

        return "{}\nTu ne possèdes pas channel".format(member.mention)

    async def limit(self, member, limit):
        data = self.load()
        if (str(member.id) in data and
                data[str(member.id)][1] != 0):
            channel = member.guild.get_channel(data[str(member.id)][1])
            if limit > 0 and limit < 100:
                data[str(member.id)][2] = limit
            else:
                data[str(member.id)][2] = None
            await channel.edit(user_limit=data[str(member.id)][2])

            self.save(data)
            return "{}\nLa limite du channel a été fixé par {}".format(
                member.mention,
                limit)

        return "{}\nTu ne possèdes pas channel".format(member.mention)

    async def permit(self, member, mentions):
        data = self.load()
        if (str(member.id) in data and
                data[str(member.id)][1] != 0):
            channel = member.guild.get_channel(data[str(member.id)][1])
            reponse = "{}\n\n".format(member.mention)
            for mention in mentions:
                await channel.set_permissions(mention,
                                              connect=True,
                                              read_messages=True)
                reponse += "-> {}\n".format(mention.mention)
            reponse += "Vous pouvez rejoindre le channel {}".format(
                data[str(member.id)][0])
            return reponse

        return "{}\nTu ne possède pas channel".format(member.mention)

    async def reject(self, member, mentions):
        data = self.load()
        if (str(member.id) in data and
                data[str(member.id)][1] != 0):
            channel = member.guild.get_channel(data[str(member.id)][1])
            reponse = "{}\n\n".format(member.mention)
            for mention in mentions:
                if mention in channel.members:
                    await mention.move_to(None)
                await channel.set_permissions(mention,
                                              connect=False,
                                              read_messages=True)
                reponse += "-> {}\n".format(mention.mention)
            reponse += "Vous ne pouvez plus rejoindre le channel {}".format(
                data[str(member.id)][0])
            return reponse

        return "{}\nTu ne possèdes pas channel".format(member.mention)

    async def claim(self, member):
        data = self.load()
        chan = member.voice
        if chan is not None:
            chan = member.voice.channel
            if (chan.category_id == 797606253479329812 and
                    chan.id != 797608077800636416):
                if (str(member.id) in data and data[str(member.id)][1] == 0):
                    for memberkey in data:
                        if data[memberkey][1] == chan.id:
                            reponse = "{}\nCe channel appartient ".format(
                                member.mention)
                            return reponse + "déjà à quelqu'un"
                    await chan.set_permissions(member,
                                               connect=True,
                                               read_messages=True,
                                               manage_channels=True)
                    data[str(member.id)][1] = chan.id
                    self.save(data)
                    reponse = "{}\nTu possèdes maintenant".format(
                        member.mention)
                    return reponse + " le channel {}".format(
                        chan.name)
                return "{}\nTu possèdes déjà le channel".format(member.mention)
            return "{}\nTu n'es pas dans un channel créé par moi".format(
                member.mention)
        return "{}\nTu n'es connecté a aucun channel".format(member.mention)


    async def commandes(self,message):

        channel = self.get_channel(861292010057105458)

        des = "Rejoins le salon vocal en dessous pour créer ton propre vocal privé,\n"
        des += f"Voici une liste des commandes que tu peux faire dans le channel \n{channel.mention} \n"
        des += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        des += "**n!voice lock** \nEmpeche plus de personnes de rejoindre le vocal\n"
        des += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        des += "**n!voice unlock** \nOuvre ton salon pour que d'autres puissent rejoindre\n"
        des += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        des += "**n!voice name <nomduchannel>** \nChange le nom du vocal\n"
        des += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        des += "**n!voice limit <nombre>** \nFixe une limite du nombre d'utilisateurs maximal pouvant rejoindre le vocal\n"
        des += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        des += "**n!voice permit <@utilisateur>** \nPermet à un utilisateur particulier de rejoindre le vocal\n"
        des += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        des += "**n!voice reject <@utilisateur>** \nEmpêche un utilisateur de rejoindre votre salon et l'expulse s'il y est déjà\n"
        des += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        des += "**n!voice claim** \nPermet de s'approprier le salon vocal si son créateur l'a quitté\n"
        des += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        
        date = datetime.datetime.now(timezone("Europe/Berlin"))
        embedVar = discord.Embed(
            title="Commandes",
            description=des,
            color=0xF7AF00,
            timestamp=date,
        )
        await message.channel.send(embed=embedVar)