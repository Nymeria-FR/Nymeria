from nymeria import nymeria
from nymeria.utility import get_guild
from nymeria.message.moderation.analyse import analyse

@nymeria.event
async def on_message(message):
    analyse(message)
    '''
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
            await message.channel.send("", file=File("donnees/logo.gif"))

        if message.content.startswith("n!infos"):
            await self.infos(message)

        if message.content.startswith("n!play"):
            if len(message.content.split(" ")) < 2:
                await message.channel.send(
                    f"{message.author.mention}\nJe n'ai pas de jeu en paramètre"
                )
                return
            game = Game(message, "n!")
            await game.launch(self)

        if message.content.startswith("n!love"):
            if len(message.content.split(" ")) < 2:
                await message.channel.send(
                    f"{message.author.mention}\nTu ne m'as donné personne en paramètre"
                )
                return
            mention = message.mentions[0].mention
            love = randint(0, 100)
            await message.channel.send(
                f"__{love}%__ d'amour entre {message.author.mention} et {mention} ❤"
            )

        if message.content.startswith("n!camion"):
            await message.delete()
            msg = message.content.split(" ")[1:]
            text = " ".join(msg)
            cam = await message.channel.send(
                f"""
──────────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───────────────▄▄██▌█ BEEP BEEP
────────────▄▄▄▌▐██▌█ {text}
────────────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
────────────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────────────▄▄██▌█ BEEP BEEP
──────────▄▄▄▌▐██▌█ {text}
──────────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──────────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
──────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───────────▄▄██▌█ BEEP BEEP
────────▄▄▄▌▐██▌█ {text}
────────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
────────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────────▄▄██▌█ BEEP BEEP
──────▄▄▄▌▐██▌█ {text}
──────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
──────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───────▄▄██▌█ BEEP BEEP
────▄▄▄▌▐██▌█ {text}
────███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
────▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─────▄▄██▌█ BEEP BEEP
──▄▄▄▌▐██▌█ {text}
──███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
──▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
───▄▄██▌█ BEEP BEEP
▄▄▄▌▐██▌█ {text}
███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀(@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─▄▄██▌█ BEEP BEEP
▄▌▐██▌█ {text}
█████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
─▄▄██▌█ BEEP BEEP
▄▌▐██▌█ {text}
█████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
──▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
▄██▌█ BEEP BEEP
▐██▌█ {text}
███▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
█▌█ BEEP BEEP
█▌█ {text}
█▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
█ BEEP BEEP
█ {text}
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
BEEP BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀(@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
EP BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
@)(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
 BEEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
(@)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
EEP
{text}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
)▀▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌
P
{text}
▄▄▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀▀▀​▀▀▀▀▀▀▌

{text}
▄▄▄▄​▄▄▄▄▄▄▌
▀▀▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
▀▀​▀▀▀▀▀▀▌

{text}
▄▄​▄▄▄▄▄▄▌
▀▀​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​▀▀▀▀▀▀▌


​▄▄▄▄▄▄▌
​▀▀▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​▀▀▀▀▌


​▄▄▄▄▌
​▀▀(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​▀▀▌


​▄▄▌
​(@)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​▌


​▌
​)▀
            """
            )
            await asyncio.sleep(1)
            await cam.edit(
                content=f"""
​


​
​
            """
            )

        if message.content.startswith("n!compte"):
            k = 1
            nb = await message.channel.send(k)
            while True:
                k += 1
                await asyncio.sleep(1)
                await nb.edit(content=k)

        if "juif" in message.content:
            await self.ban_word(message)

        if "negro" in message.content:
            await self.ban_word(message)

        if "nez gros" in message.content:
            await self.ban_word(message)

        if "nazi" in message.content:
            await self.ban_word(message)

        if "negre" in message.content:
            await self.ban_word(message)

        if "pd" in message.content:
            await self.ban_word(message)

        if message.content.startswith("n!stats"):

            def fortnite_tracker_api(platform, nickname):
                URL = (
                    "https://api.fortnitetracker.com/v1/profile/"
                    + platform
                    + "/"
                    + nickname
                )
                req = requests.get(URL, headers={"TRN-Api-Key": config.token_ftn})

                if req.status_code == 200:
                    try:
                        # print(req.json())
                        lifetime_stats = req.json()["lifeTimeStats"]
                        return lifetime_stats[7:]
                    except KeyError:
                        return False
                else:
                    return False

            words = message.content.split(" ", 2)

            if len(words) < 3:
                await self.send_message(
                    message.channel, "Usage: " + "n!" + "stats <pc,xbl,psn> <nickname>"
                )
                return

            platform = words[1].lower()

            # more acceptable platform names
            if platform == "xbox":
                platform = "xbl"
            elif platform == "ps4":
                platform = "psn"

            if platform not in ("pc", "xbl", "psn"):
                await self.send_message(
                    message.channel,
                    "Usage: " + COMMAND_PREFIX + "stats <pc,xbl,psn> <nickname>",
                )
                return
            else:
                res = fortnite_tracker_api(platform, words[2])

                if res:
                    matches_played = res[0]["value"]
                    wins = res[1]["value"]
                    win_percent = res[2]["value"]
                    kills = res[3]["value"]
                    kd = res[4]["value"]

                    embed = discord.Embed(
                        title="__Stats Fortnite de " + words[2] + "__", color=0xF7AF00
                    )

                    embed.add_field(
                        name="Parties jouées", value=matches_played + "\n", inline=False
                    )
                    embed.add_field(name="Victoires", value=wins + "\n", inline=False)
                    embed.add_field(
                        name="Pourcentage de victoire",
                        value=win_percent + "\n",
                        inline=False,
                    )
                    embed.add_field(name="Kills", value=kills + "\n", inline=False)
                    embed.add_field(name="K/D", value=kd + "\n", inline=False)
                    await message.channel.send(embed=embed)
                    if float(kd) < 1:
                        await message.channel.send("Pas fou le K/D hein")
                else:
                    await message.channel.send(
                        "Je n'ai pas pu trouvé de données pour cet utilisateur."
                    )
'''