import discord
import datetime
from pytz import timezone
from random import randint


from mod import Moderation
from voc import Voice
from game import Game

class Bot(discord.Client, Moderation, Voice):
    def __init__(self, Myintents):
        self.invites = list()
        discord.Client.__init__(self, intents=Myintents)
        Voice.__init__(self)

    async def on_ready(self):
        """
        event when the bot is ready
        Parameters
        ----------
        Return
        ------
        None
        """
        print("Load")
        self.__guild_suport = self.get_guild(861292008101642281)
        self.__channel_logs = self.__guild_suport.get_channel(861292008667742213)
        self.guild = self.get_guild(861292008101642281)
        self.invites = await self.guild.invites()

        date = datetime.datetime.now(timezone("Europe/Berlin"))
        embedVar = discord.Embed(
            title="Ready",
            description=f"Logged as {self.user}",
            color=0xF7AF00,
            timestamp=date,
        )
        await self.__channel_logs.send(embed=embedVar)
        await self.reload_member_count()

    async def on_invite_create(self, invite):
        self.invites = await self.guild.invites()

    async def on_invite_delete(self, invite):
        self.invites = await self.guild.invites()   

    async def get_inviter(self):
        new_invite = await self.guild.invites()
        for i in range(len(new_invite)):
            if new_invite[i].uses > self.invites[i].uses:
                return new_invite[i].inviter

    async def reload_member_count(self):
        count_channel: discord.VoiceChannel = self.get_channel(
            862112173168918538)
        for guild in self.guilds:
            if guild.id == 861292008101642281:
                total_member = guild.member_count
        newname = "Membres: {}".format(str(total_member))
        await count_channel.edit(name=newname)

    async def welcome_message(self, member, inviter):

        welcome_channel: discord.TextChannel = self.get_channel(861292008910749705)
        rules_channel: discord.TextChannel = self.get_channel(861292008910749698)
        date = datetime.datetime.now(timezone("Europe/Berlin"))
        embedVar = discord.Embed(
            title="Bienvenue !",
            description="→ Oh ! {} vient de nous rejoindre ! ← \n \n・Souhaitez lui la bienvenue ! \n・Pense à prendre tes rôles dans {} \n \n・Tu as utilisé l'invitation de **{}** ".format(
                member.mention, rules_channel.mention, inviter.name
            ),
            color=0xF7AF00,
            timestamp=date,
        )
        await welcome_channel.send(embed=embedVar)

    async def on_member_join(self, member):
        inviter = await self.get_inviter()
        bot = await self.add_bot_role(member)
        if bot is False:
            await self.welcome_message(member, inviter)
            await self.add_member_role(member)
        await self.reload_member_count()
        self.invites = await self.guild.invites()
    
    async def on_member_remove(self,member):
        await self.reload_member_count()

    async def on_message(self, message):
        """
        event when the bot detecte new message
        Paramaters
        ----------
        message : discord.Message
            message recive

        Return
        ------
        None
        """
        if message.content.startswith("n!voice"):
            await message.channel.send(await self.voiceCommande(message))
            return
        if message.content.startswith("n!pp"):
            pfp = message.author.avatar_url
            await message.channel.send(pfp)

        if "quoi" in message.content:
            await message.channel.send("feur")

        if "ping" in message.content:
            await message.channel.send("pong")

        if "pong" in message.content:
            await message.channel.send("ping")
        
        if message.content.startswith("n!reload"):
            await self.reload_member_count()
        
        if message.content.startswith("n!del"):
            await self.deleteMessage(message)
            
        if message.content.startswith("n!ban"):
            await self.ban(message)
        
        if message.content.startswith("n!ub"):
            await self.unban(message)
        
        if message.content.startswith("n!kick"):
            await self.kick(message)
        
        if message.content.startswith("n!mute"):
            await self.mute(message)
        
        if message.content.startswith("n!um"):
            await self.unmute(message)
        
        if message.content.startswith("n!banlist"):
            await self.banlist(message)
        
        if(message.content.startswith("n!play")):
            if len(message.content.split(' ')) < 2:
                await message.channel.send(f"{message.author.mention}\nI do not have a game in parameter")
                return
            game = Game(message, "n!")
            await game.launch(self)
        
        if(message.content.startswith("n!love")):
            if len(message.content.split(' ')) < 2:
                await message.channel.send(f"{message.author.mention}\nYou didn't give me a person")
                return
            mention = message.mentions[0].mention
            love = randint(0,100)
            await message.channel.send(f"__{love}%__ of love between {message.author.mention} and {mention} ❤")
        
        if(message.content.startswith("n!emote")):
            await self.emote(message)
