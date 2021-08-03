import requests
from discord import Embed
from nymeria import config


async def fortnite_stat(message):
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
        await message.channel.send(
            "Usage: " + "n!" + "fortnite <pc,xbl,psn> <nickname>"
        )
        return

    platform = words[1].lower()

    # more acceptable platform names
    if platform == "xbox":
        platform = "xbl"
    elif platform == "ps4":
        platform = "psn"

    if platform not in ("pc", "xbl", "psn"):
        await message.channel.send(
            "Usage: n!fortnite <pc,xbl,psn> <nickname>",
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

        embed = Embed(
            title="__Stats Fortnite de " + words[2] + "__", color=0xF7AF00
        )

        embed.add_field(
            name="Parties jouées", value=matches_played + "\n", inline=False
        )
        embed.add_field(name="Victoires",
                        value=wins + "\n", inline=False)
        embed.add_field(
            name="Pourcentage de victoire",
            value=win_percent + "\n",
            inline=False,
        )
        embed.add_field(
            name="Kills", value=kills + "\n", inline=False)
        embed.add_field(name="K/D", value=kd + "\n", inline=False)
        await message.channel.send(embed=embed)
        if float(kd) < 1:
            await message.channel.send("Pas fou le K/D hein")
    else:
        await message.channel.send(
            "Je n'ai pas pu trouver de données pour cet utilisateur."
        )
