import datetime

from pytz import timezone
from discord import Streaming, Embed

from nymeria.join import get_invites
from . import nymeria, config


@nymeria.event
async def on_ready():
    print("Logged as {}!".format(nymeria.user))
    await nymeria.change_presence(
        activity=Streaming(
            name="discord.gg/nymeria", url="https://www.twitch.tv/mohasama_"
        )
    )
    channel_logs = nymeria.get_channel(config.ready_chan)

    date = datetime.datetime.now(timezone("Europe/Berlin"))
    embedVar = Embed(
        title="Ready",
        url="http://www.nymeria.org/",
        description=(f"Logged as {nymeria.user}"),
        color=0xF7AF00,
        timestamp=date,
    )
    embedVar.set_author(
        name="Nymeria",
        url="http://nymeria.org/",
        icon_url="https://avatars.githubusercontent.com/u/87084249?s=200&v=4",
    )
    embedVar.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/861292008910749705/862528074373529600/logo.gif"
    )
    await channel_logs.send(embed=embedVar)
    await get_invites()