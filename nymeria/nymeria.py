import discord
import datetime
from discord import File
from discord import Button, Select, SelectOption
from pytz import timezone
from random import randint
from config import TomlConfig, config
import requests


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
        #activity = discord.Game(name="discord.gg/nymeria", type=3)
        #await self.change_presence(status=discord.Status.idle, activity=activity)
        await self.change_presence(activity=discord.Streaming(name='discord.gg/nymeria', url='https://www.twitch.tv/mohasama_'))
        self.__guild_suport = self.get_guild(861292008101642281)
        self.__channel_logs = self.__guild_suport.get_channel(861292010057105466)
        self.guild = self.get_guild(861292008101642281)
        self.invites = await self.guild.invites()

        date = datetime.datetime.now(timezone("Europe/Berlin"))
        embedVar = discord.Embed(
            title="Ready",
            url = "http://www.nymeria.org/",
            description=f"Logged as {self.user}",
            color=0xF7AF00,
            timestamp=date,
        )
        embedVar.set_author(name="Boubou", url="https://twitter.com/BoubouSW",icon_url="https://cdn.discordapp.com/avatars/303935152071901184/cb7644ce9aeb0cd703bb4dd29ff2e52a.webp?size=1024")
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/861292008910749705/862528074373529600/logo.gif")
        #embedVar.set_image(url="https://cdn.discordapp.com/attachments/861292008910749705/862528074373529600/logo.gif")
        await self.__channel_logs.send(embed=embedVar,components = [Button(label = "test")])
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
            url = "http://www.nymeria.org/",
            description="→ Oh ! {} vient de nous rejoindre ! ← \n \n・Souhaitez lui la bienvenue ! \n・Pense à prendre tes rôles dans {} \n \n・Tu as utilisé l'invitation de **{}** ".format(
                member.mention, rules_channel.mention, inviter.name
            ),
            color=0xF7AF00,
            timestamp=date,
        )
        embedVar.set_thumbnail(url=f'{member.avatar_url}')
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
            reponse = await self.voiceCommande(message)
            if type(reponse) != None and reponse != "":
                await message.channel.send(reponse)
            return
        if message.content.startswith("n!pp"):
            if len(message.mentions) == 0:
                pp = message.author.avatar_url
                await message.channel.send(pp)
                return
            else:
                for mention in message.mentions:
                    pp = mention.avatar_url
                    await message.channel.send(pp)
        
        if message.content.startswith("n!reload"):
            await self.reload_member_count()
        
        if message.content.startswith("n!logo"):
            await message.channel.send("",file=File('donnees/logo.gif'))

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
        
        if message.content.startswith("n!infos"):
            await self.infos(message)

        if(message.content.startswith("n!play")):
            if len(message.content.split(' ')) < 2:
                await message.channel.send(f"{message.author.mention}\nJe n'ai pas de jeu en paramètre")
                return
            game = Game(message, "n!")
            await game.launch(self)
        
        if(message.content.startswith("n!love")):
            if len(message.content.split(' ')) < 2:
                await message.channel.send(f"{message.author.mention}\nTu ne m'as donné personne en paramètre")
                return
            mention = message.mentions[0].mention
            love = randint(0,100)
            await message.channel.send(f"__{love}%__ d'amour entre {message.author.mention} et {mention} ❤")
        
        if(message.content.startswith("n!camion")):
            await message.delete()
            msg = message.content.split(' ')[1:]
            text = " ".join(msg)
            await message.channel.send(f"""
──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───▄▄██▌█ BEEP BEEP
▄▄▄▌▐██▌█ {text}
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
 ▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """)

        if(message.content.startswith("n!emote")):
            await self.emote(message)

        if("juif" in message.content):
            await self.ban_word(message)
        
        if("negro" in message.content):
            await self.ban_word(message)
        
        if("nez gros" in message.content):
            await self.ban_word(message)
        
        if("nazi" in message.content):
            await self.ban_word(message)
        
        if("negre" in message.content):
            await self.ban_word(message)
        
        if("pd" in message.content):
            await self.ban_word(message)


        if message.content.startswith('n!stats'):

            def fortnite_tracker_api(platform, nickname):
                URL = 'https://api.fortnitetracker.com/v1/profile/' + platform + '/' + nickname
                req = requests.get(URL, headers={"TRN-Api-Key": config.token_ftn})

                if req.status_code == 200:
                    try:
                        #print(req.json())
                        lifetime_stats = req.json()['lifeTimeStats']
                        return lifetime_stats[7:]
                    except KeyError:
                        return False
                else:
                    return False


            words = message.content.split(' ', 2)

            if len(words) < 3:
                await self.send_message(message.channel, 'Usage: ' + 'n!' + 'stats <pc,xbl,psn> <nickname>')
                return

            platform = words[1].lower()

            # more acceptable platform names
            if platform == 'xbox':
                platform = 'xbl'
            elif platform == 'ps4':
                platform = 'psn'

            if platform not in ('pc','xbl','psn'):
                await self.send_message(message.channel, 'Usage: ' + COMMAND_PREFIX + 'stats <pc,xbl,psn> <nickname>')
                return
            else:
                res = fortnite_tracker_api(platform,words[2])

                if res:
                    matches_played = res[0]['value']
                    wins = res[1]['value']
                    win_percent = res[2]['value']
                    kills = res[3]['value']
                    kd = res[4]['value']

                    embed = discord.Embed(title="__Stats Fortnite de " + words[2] + "__", color=0xF7AF00)

                    embed.add_field(name="Parties jouées", value=matches_played + '\n', inline=False)
                    embed.add_field(name="Victoires", value=wins + '\n', inline=False)
                    embed.add_field(name="Pourcentage de victoire", value=win_percent + '\n', inline=False)
                    embed.add_field(name="Kills", value=kills + '\n', inline=False)
                    embed.add_field(name="K/D", value=kd + '\n', inline=False)
                    await message.channel.send(embed=embed)
                    if float(kd) < 1:
                        await message.channel.send("Pas fou le K/D hein")
                else:
                    await message.channel.send("Je n'ai pas pu trouvé de données pour cet utilisateur.")